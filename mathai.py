class Matrix:
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for i in range(cols)] for j in range(rows)]
    def __str__(self):
        return str(self.data)
    def __add__(self,other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows,self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            return "Invalid Operation"
    def __sub__(self,other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows,self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] - other.data[i][j]
            return result
        else:
            return "Invalid Operation"
    def __mul__(self,other):
        if self.cols == other.rows:
            result = Matrix(self.rows,other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(other.rows):
                            result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            return "Invalid Operation"
    
    def print(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.data[i][j],end=" ")
            print()

    def __getitem__(self,index):
        return self.data[index]
    
    def scalar(self,other):
        result = Matrix(self.rows,other.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] += self.data[i][j] * other.data[i][j]
        return result
    
    

A = Matrix(3,3)
A.data = [[1,2,3],[1,2,1],[3,2,0]]

B = Matrix(3,3)
B.data = [[4,1,2],[0,4,3],[1,1,1]]

p = Matrix(3,1)
p.data = [[0.1],[1.7],[-1.5]]

q = Matrix(3,1)
q.data = [[-1.6],[0.8],[1.1]]

r = Matrix(3,1)
r.data = [[-0.7],[1.3],[0.2]]

plus = q - p
plus1 = plus - r
plus2 = B * plus1

res = plus2.scalar(q)

sum = 0
for i in range(res.rows):
    for j in range(res.cols):
        sum += res[i][j]
print("%.2f" % sum)