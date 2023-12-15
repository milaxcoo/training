import numpy as np


coefficients = np.array([
    [2, -4, 3],
    [3, -1, 5],
    [1, -2, 4]
]) #А


constants = np.array([1, 2, 3]) #строчка В


solution = np.linalg.solve(coefficients, constants)


x, y, z = solution


print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")