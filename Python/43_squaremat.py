def cvt_to_square(mat):
    N, M = len(mat), len(mat[0])
    if N == M:
        return mat
    elif N > M:
        result = mat.copy()
        rm = N - M
        for i in range(rm):
            result.pop(i)
        return result
    else:
        result = mat.copy()
        rm = M - N
        for vector in mat:
            for i in range(1, rm+1):
                vector.pop(i)
        return result
    

def input_matrix():
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    return matrix

def main():
    mat = input_matrix()
    mat = cvt_to_square(mat)
    
    for vector in mat:
        print(' '.join(map(str, vector)))
        
main()