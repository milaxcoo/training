import numpy as np
from scipy.optimize import linear_sum_assignment

# Заданная матрица эффективности
matrix = np.array([
    [3, 5, 2, 6, 4],
    [4, 7, 1, 3, 8],
    [6, 3, 9, 2, 5],
    [2, 8, 6, 4, 3],
    [5, 2, 4, 7, 6]
])

# Применение метода Хунгари для поиска оптимального назначения
row_indices, col_indices = linear_sum_assignment(matrix)

# Вывод оптимального назначения
for row, col in zip(row_indices, col_indices):
    print(f"Строка {row + 1} назначается на столбец {col + 1} с эффективностью {matrix[row, col]}")

# Вывод общей эффективности
total_efficiency = matrix[row_indices, col_indices].sum()
print(f"\nОбщая эффективность: {total_efficiency}")
