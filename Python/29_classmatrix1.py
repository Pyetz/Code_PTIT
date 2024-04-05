class Matrix:
    def __init__(self, n, m, matrix):
        self.n = n
        self.m = m
        self.matrix = matrix

    def transpose(self):
        transposed = []
        for i in range(self.m):
            transposed.append([self.matrix[j][i] for j in range(self.n)])
        return Matrix(self.m, self.n, transposed)
        
    def product(self, other):
        if self.m != other.n:
            return None
        product = []
        for i in range(self.n):
            product.append([])
            for j in range(other.m):
                product[i].append(sum([self.matrix[i][k] * other.matrix[k][j] for k in range(self.m)]))
        return Matrix(self.n, other.m, product)

def input_matrix(tess):
    matrices = []
    for _ in range(tess):
        n, m = map(int, input().split())
        matrix = []
        for j in range(n):
            matrix.append(list(map(int, input().split())))
        matrices.append(Matrix(n, m, matrix))
    return matrices

def print_matrix(mat):
    for row in mat.matrix:
        print(' '.join(map(str, row)))

def main():
    tess = int(input())
    matrices = input_matrix(tess)
    for mat in matrices:
        transposed_mat = mat.transpose()
        product_mat = mat.product(transposed_mat)
        print_matrix(product_mat)

main()
