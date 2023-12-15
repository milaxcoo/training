def determinant(matrix):
    return matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] + matrix[0][2] * matrix[1][0] * matrix[2][1] - matrix[0][2] * matrix[1][1] * matrix[2][0] - matrix[0][1] * matrix[1][0] * matrix[2][2] - matrix[0][0] * matrix[1][2] * matrix[2][1]


def kramer(matrix, vector):
    det = determinant(matrix)
    if det == 0:
        return "Система не имеет единственного решения (определитель матрицы равен 0)"
    
    matrix_x = [
        [vector[0], matrix[0][1], matrix[0][2]],
        [vector[1], matrix[1][1], matrix[1][2]],
        [vector[2], matrix[2][1], matrix[2][2]]
    ]

    matrix_y = [
        [matrix[0][0], vector[0], matrix[0][2]],
        [matrix[1][0], vector[1], matrix[1][2]],
        [matrix[2][0], vector[2], matrix[2][2]]
    ]

    matrix_z = [
        [matrix[0][0], matrix[0][1], vector[0]],
        [matrix[1][0], matrix[1][1], vector[1]],
        [matrix[2][0], matrix[2][1], vector[2]]
    ]

    x = determinant(matrix_x) / det
    y = determinant(matrix_y) / det
    z = determinant(matrix_z) / det

    return x, y, z


matrix = [
    [2, -4, 3],
    [3, -1, 5],
    [1, -2, 4]
]
vector = [1, 2, 3]

solution = kramer(matrix, vector)
print("(x, y, z) =", solution)
