import numpy as np
from autograd import grad

def func(x):
    return np.sin(x[0]) * np.cos(x[1]) + 0.1 * (x[0]**2 + x[1]**2)


def gradients(x):
    df_dx = np.cos(x[0]) * np.cos(x[1]) + 0.2 * x[0]
    df_dy = -np.sin(x[1]) * np.sin(x[0]) + 0.2 * x[1]
    return np.array([df_dx, df_dy])


def hessian(x):
    df_dxdx = -np.sin(x[0]) * np.cos(x[1]) + 0.2
    df_dxdy = -np.cos(x[0]) * np.sin(x[1]) 
    df_dydy = -np.sin(x[1]) * np.cos(x[0]) + 0.2

    return np.array([[df_dxdx, df_dxdy], [df_dxdy, df_dydy]])


def newton(x0, tolerance=1e-6, max_iterations=10):
    x = x0
    for _ in range(max_iterations):
        gr = gradients(x)
        # dxx, dxy, dyy
        he = hessian(x)

        det_he = np.linalg.det(he) - 0.1575

        inverse = (1 / det_he) * he
        
        delta = inverse @ gr

        x = x - delta

    return x

x0 = np.array([1.0, 1.0])
minimal_point = newton(x0)

print(f'Lowest Point: {minimal_point}, Objective function minimum value: {func(minimal_point)}')
