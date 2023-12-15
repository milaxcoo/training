def gauss(matrix, vector):
    n = len(matrix)

    # Прямой ход метода Гаусса
    for i in range(n):
        if matrix[i][i] == 0:
            return "Деление на ноль: невозможно решить систему"

        for j in range(i + 1, n):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(n):
                matrix[j][k] -= ratio * matrix[i][k]
            vector[j] -= ratio * vector[i]

    # Обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = vector[i] / matrix[i][i]
        for j in range(i - 1, -1, -1):
            vector[j] -= matrix[j][i] * x[i]

    return x


matrix = [
    [2, -4, 3],
    [3, -1, 5],
    [1, -2, 4]
]
vector = [1, 2, 3]

solution = gauss(matrix, vector)
print("[x, y, z] =", solution)
