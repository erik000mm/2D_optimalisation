import numpy as np

def func(x):
    return (x[0] - 2) ** 2 + (x[1] - 3) ** 2


def optimize_function(x0, directions, max_iterations=100, tolerance=1e-6):
    x = x0

    for iteration in range(max_iterations):
        previous_value = func(x)

        # minimalise function in direction dir_i
        for i in range(len(directions)):
            dir_i = directions[i]
            alpha_values = np.linspace(-5, 5, 100)
            f_values = [func(x + alpha * dir_i) for alpha in alpha_values]

            x += alpha_values[np.argmin(f_values)] * dir_i
        
        # new direction
        new_direction = x - directions[0]
        
        # replace longest original direction with new
        lengths = [np.linalg.norm(d) for d in directions]
        longest_index = np.argmax(lengths)
        directions[longest_index] = new_direction
        
        current_value = func(x)
        
        if abs(current_value - previous_value) < tolerance:
            print(f'Termination condition met after {iteration} iterations.')
            break

    return x

x0 = np.array([0.0, 0.0])
initial_directions = [np.array([1.0, 0.0]), np.array([0.0, 1.0])]
result = optimize_function(x0, directions=initial_directions)
print(f'Optimal points: {result}, Objective function minimum value: {func(result)}')