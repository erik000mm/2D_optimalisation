import numpy as np


def func(x):
    return x[0]**2 + x[1]**2

def gradients(x):
    df_dx = 2*x[0]
    df_dy = 2*x[1]

    return np.array([df_dx, df_dy])


def descent(x0, alpha=0.1, epsilon=0.0001, max_iterations=100):
    x = x0

    for _ in range(max_iterations):
        gradient = gradients(x)

        if np.linalg.norm(gradient) < epsilon:
            return x
        
        x = x - alpha * gradient

    return x


x0 = np.array([2, 2])
minimal_point = descent(x0)
print(f'Lowest Point: {minimal_point}, Objective function minimum value: {func(minimal_point)}')
        