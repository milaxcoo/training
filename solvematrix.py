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



#without numpy



def gauss(matrix):
    n = len(matrix)
    
    for i in range(n):
        max_elem = abs(matrix[i][i])
        max_row = i

        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_elem:
                max_elem = abs(matrix[k][i])
                max_row = k

        for k in range(i, n + 1):
            temp = matrix[max_row][k]
            matrix[max_row][k] = matrix[i][k]
            matrix[i][k] = temp

        for k in range(i + 1, n):
            factor = -matrix[k][i] / matrix[i][i]
            for j in range(i, n + 1):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += factor * matrix[i][j]

    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            matrix[k][n] -= matrix[k][i] * x[i]

    return x


equations = [
    [2, -4, 3, 1],
    [3, -1, 5, 2],
    [1, -2, 4, 3]
]


solution = gauss(equations)


print(f"x = {solution[0]}")
print(f"y = {solution[1]}")
print(f"z = {solution[2]}")
