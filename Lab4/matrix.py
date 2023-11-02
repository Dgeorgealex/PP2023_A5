class Matrix:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for _ in range(self.m)] for _ in range(self.n)]

    def set(self, i, j, value):
        self.matrix[i][j] = value

    def get(self, i, j):
        return self.matrix[i][j]

    def __mul__(self, other):
        ans = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                ans.matrix[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.m))
        return ans

    def transpose(self):
        trans = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                trans.matrix[j][i] = self.matrix[i][j]
        return trans

    def modify(self, f):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = f(self.matrix[i][j])

    def __str__(self):
        my_string = ""
        for i in range(self.n):
            for j in range(self.m):
                my_string += str(self.matrix[i][j]) + " "
            my_string += "\n"
        return my_string


if __name__ == "__main__":
    matrix = Matrix(2, 3)
    matrix.set(1, 2, -1)
    matrix.set(0, 2, 4)
    matrix.set(0, 0,  5)
    print(matrix)

    transpose = matrix.transpose()
    print(transpose)

    multiply = matrix * transpose
    print(multiply)

    multiply.modify(lambda x: x - 10)
    print(multiply)
