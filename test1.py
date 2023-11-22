class Matrix:
    #конструктор
    def __init__(self, matrix):
        self.matrix = matrix

    #методы подписаны
    def determinant(self):
        if len(self.matrix) == 1:
            return self.matrix[0][0]
            #easy way
        else:
            det = 0
            for i in range(len(self.matrix)):
                det += self.matrix[0][i] * self.cofactor(0, i)
            return det
        
    #сборка матрицы из миноров
    def cofactor(self, i, j):
        return (-1) ** (i + j) * self.minor(i, j).determinant()
        
    def minor(self, i, j):
        matrix = []
        for m in range(len(self.matrix)):
            if m != i:
                row = []
                for n in range(len(self.matrix[0])):
                    if n != j:
                        row.append(self.matrix[m][n])
                matrix.append(row)
        return Matrix(matrix)
    
    def transpose(self):
        return Matrix([[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))])
    
    #вывод
    def show(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print('%i ' % self.matrix[i][j], end = "")
            print()
    
    
a = Matrix([[3, 0, -1], [2, 1, 0], [-4, -1, 1]])
a.show()
print(a.determinant())
b = a.transpose()
b.show()