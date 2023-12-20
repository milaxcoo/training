#multiply float digit by float matrix
def multiply_digit_by_matrix(digit, matrix):
    result = [0] * len(matrix)
    for i in range(len(matrix)):
        result[i] = digit * matrix[i]
    return result

a = 1/136.185

print(multiply_digit_by_matrix(a, [60.346, -106.326, 59.996]))
