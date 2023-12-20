
A = [[46, -30, 32],
     [-30, 108, -30],
     [32, -30, 46]]

initial_guess = [1, 0, 0]

max_iterations = 3
tolerance = 1e-8

def matrix_vector_multiplication(matrix, vector):
    result = [0] * len(vector)
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result

def dot_product(vector1, vector2):
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result

def scalar_vector_multiplication(scalar, vector):
    result = [0] * len(vector)
    for i in range(len(vector)):
        result[i] = scalar * vector[i]
    return result

def normalize_vector(vector):
    norm = (sum(x ** 2 for x in vector)) ** 0.5
    return [x / norm for x in vector]

def power_iteration(matrix, initial_vector, max_iterations, tolerance):
    eigenvalue = 0
    eigenvector = initial_vector.copy()

    for i in range(max_iterations):
        
        new_vector = matrix_vector_multiplication(matrix, eigenvector)

        new_eigenvalue = dot_product(new_vector, eigenvector)

        new_vector = normalize_vector(new_vector)

        if abs(new_eigenvalue - eigenvalue) < tolerance:
            break

        eigenvalue = new_eigenvalue
        eigenvector = new_vector

    return eigenvalue, eigenvector

max_eigenvalue, max_eigenvector = power_iteration(A, initial_guess, max_iterations, tolerance)

print("Максимальное по модулю собственное значение:", max_eigenvalue)
print("Соответствующий собственный вектор:", max_eigenvector)