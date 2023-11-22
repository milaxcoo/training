
import numpy as np

def find_determinant(matrix):
    return np.linalg.det(matrix)

def transpose_matrix(matrix):
    return np.transpose(matrix)


a = np.array([[3, 0, -1], [2, 1, 0], [-4, -1, 1]])

print("A = ")
print(a)
print("Determinant is %i" % find_determinant(a))
print("Transposed: ")
print(transpose_matrix(a))

