import numpy as np
from scipy.linalg import eig

A = np.array([[46, -30, 32],
              [-30, 108, -30],
              [32, -30, 46]])

cos_squared_A = np.cos(A) ** 2

def arcsin_matrix(matrix):
    return np.arcsin(np.clip(matrix, -1, 1))

result_matrix = arcsin_matrix(cos_squared_A)

eigenvalues, eigenvectors = eig(A)

print("Матрица T (собственные векторы):")
print(eigenvectors)
print("\nМатрица J (собственные числа):")
print(np.diag(eigenvalues))
print("\nМатрица f(J):")
print(arcsin_matrix(np.diag(eigenvalues)))
print("\nМатрица f(A):")
print(result_matrix)
