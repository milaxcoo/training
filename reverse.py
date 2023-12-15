def matrix_inverse(matrix):
    det = matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] + matrix[0][2] * matrix[1][0] * matrix[2][1] - matrix[0][2] * matrix[1][1] * matrix[2][0] - matrix[0][1] * matrix[1][0] * matrix[2][2] - matrix[0][0] * matrix[1][2] * matrix[2][1]
    if det == 0:
        return None  # Система не имеет обратной матрицы (нулевой определитель)

    inv_det = 1.0 / det

    inverse = [
        [(matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]) * inv_det,
         (matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) * inv_det,
         (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) * inv_det],
        [(matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) * inv_det,
         (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) * inv_det,
         (matrix[1][0] * matrix[0][2] - matrix[0][0] * matrix[1][2]) * inv_det],
        [(matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1]) * inv_det,
         (matrix[2][0] * matrix[0][1] - matrix[0][0] * matrix[2][1]) * inv_det,
         (matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]) * inv_det]
    ]

    return inverse

def solve(matrix, vector):
    inverse = matrix_inverse(matrix)
    if inverse is None:
        return "Система не имеет обратной матрицы (нулевой определитель)"
    
    result = [
        sum(inverse[i][j] * vector[j] for j in range(3)) for i in range(3)
    ]
    return result



matrix = [
    [2, -4, 3],
    [3, -1, 5],
    [1, -2, 4]
]
vector = [1, 2, 3]

solution = solve(matrix, vector)
print("[x, y, z] =", solution)
