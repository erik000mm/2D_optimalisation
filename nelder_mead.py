import numpy as np


def func(x):
    return ((x[0]-1)**2 + (x[1]-2)**2)


def nelder_mead(points, max_iterations=100, tolerance=1e-6):
    for iteration in range(max_iterations):
        f_points = []

        # Calculating points based on function f
        for point in points:
            f_points.append([func(point[0]), point[1]])

        # Sort the points
        sorted_f_points = sorted(f_points, key=lambda x: x[0])

        if sorted_f_points[-1][0] - sorted_f_points[0][0] < tolerance:
            print(f'Termination condition met after {iteration} iterations.')
            break

        # Worst point based on f
        worst_f_point = sorted_f_points[-1]

        # Worst point
        worst_point = next((sub for sub in points if sub[1] == worst_f_point[1]), None)

        filtered_array = [item for item in points if item[1] != worst_point[1]]

        center = sum(pair[0] for pair in filtered_array)/2

        # Try reflexion 
        xr = center + 1 * (center - worst_point[0])
        f_xr = func(xr)

        new_points = []

        if f_xr < sorted_f_points[0][0]:
            # try expansion
            xe = center + 2 * (xr - center)
            f_xe = func(xe)
            
            # If expanded point better than reflected
            if f_xe < f_xr:
                filtered_array.append([xe, worst_point[1]])
            else:
                filtered_array.append([xr, worst_point[1]])

        elif f_xr < sorted_f_points[1][0] and f_xr >= sorted_f_points[0][0]:
            # accept reflexion
            filtered_array.append([xr, worst_point[1]])
        elif f_xr >= worst_f_point[0]:
            # try contraction
            xc = center + 0.5 * (worst_point[0] - center)
            f_xc = func(xc)

            if f_xc < f_xr:
                filtered_array.append([xc, worst_point[1]])
        else:
            # Filter the best
            best_value = sorted_f_points[0]
            best_point = next((sub for sub in points if sub[1] == sorted_f_points[0][1]), None)

            missing_points = [item[1] for item in sorted_f_points if item != best_value]

            sorted_f_points.pop(0)
            farray = sorted_f_points

            for index, point in enumerate(farray):
                xs = np.array([0, 0])
                xs = best_point[0] + 0.5 * (point[0] - best_point[0])
                new_points.append([xs, missing_points[index]])

            new_points.append(best_point)

        if new_points:
            points = new_points
        else:
            points = filtered_array

    return points

points = [[np.array([0, 0]), 'A'], [np.array([2, 0]), 'B'], [np.array([0, 3]), 'C']]

new_points = nelder_mead(points=points)

def find_lowest_point(points):
    lowest_point = None
    min_distance = float('inf')
    
    for point, label in points:
        distance = np.linalg.norm(point)
        if distance < min_distance:
            min_distance = distance
            lowest_point = (point, label)
    
    return lowest_point


lowest_point = find_lowest_point(new_points)

print(f'Lowest Point: {lowest_point[0]}, Objective function minimum value: {func(lowest_point[0])}')