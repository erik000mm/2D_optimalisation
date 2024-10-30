import numpy as np


def find_max_and_index(lst):
    max_value = max(lst)
    max_index = len(lst) - 1 - lst[::-1].index(max_value)
    
    return max_value, max_index


def func(x):
    return ((x[0]-1)**2 + (x[1]-2)**2)


def nelder_mead(points):
    # ordering by function
    calculated_points = []

    for point in points:
        calculated_points.append([func(point[0]), point[1]])

    max_point, max_index = find_max_and_index(calculated_points)
    worst_number = calculated_points[max_index]
    points.pop(max_index)
    
    # calculate center without worst point
    x_sum = sum(pair[0] for pair in points)

    center = x_sum/2

    # try reflexion c + alpha * (c - A/B/C)
    xr = center + 1 * (center - max_point[0])

    f_xr = func(xr)

    second_best = min(points[0])

    # If then try contraction
    if f_xr > worst_number:
        xc = center + 0.5 * (max_point[0] - center)
        f_xc = func(xc)
        """
        if f_xc > worst_number:
            print()
        else:
            print("point better")
            points.append(xc)
        """




    print()

points = [[np.array([0, 0]), 'A'], [np.array([2, 0]), 'B'], [np.array([0, 3]), 'C']]

nelder_mead(points=points)