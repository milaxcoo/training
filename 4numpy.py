import numpy as np

A = np.array([[46, -30, 32],
              [-30, 108, -30],
              [32, -30, 46]])

initial_guess = np.array([1, 0, 0])

max_iterations = 3
tolerance = 1e-8

def power_iteration(matrix, initial_vector, max_iterations, tolerance):
    eigenvalue = 0
    eigenvector = initial_vector

    for i in range(max_iterations):
        # умножаем матрицу на текущий собственный вектор
        new_vector = np.dot(matrix, eigenvector)

        # находим новое приближение собственного значения
        new_eigenvalue = np.dot(new_vector, eigenvector)
        
        # нормализуем вектор
        new_vector = new_vector / np.linalg.norm(new_vector)

        # проверяем насколько сильно изменилось собственное значение
        if np.abs(new_eigenvalue - eigenvalue) < tolerance:
            break

        eigenvalue = new_eigenvalue
        eigenvector = new_vector

    return eigenvalue, eigenvector

# метод степенных итераций
max_eigenvalue, max_eigenvector = power_iteration(A, initial_guess, max_iterations, tolerance)

print("Максимальное по модулю собственное значение:", max_eigenvalue)
print("Соответствующий собственный вектор:", max_eigenvector)
