def lucky_num_of_mat(matrix):
    max_val, min_val = -1, -1
    for vector in matrix:
        if max_val == -1 or max(vector) > max_val:
            max_val = max(vector)
        if min_val == -1 or min(vector) < min_val:
            min_val = min(vector)
    return abs(max_val - min_val)

def find_lucky_num(matrix, lucky_num):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == lucky_num:
                result.append((i, j))
    return result


def input_matrix():
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        lst = list(map(int, input().split()))
        for i in range(M, len(lst)):
            lst.pop(i)
        matrix.append(lst)
            
    return matrix

def main():
    mat = input_matrix()
    luckynum = lucky_num_of_mat(mat)
    luckynumpos = find_lucky_num(mat, luckynum)
    
    if len(luckynumpos) == 0:
        print('NOT FOUND')
    else:
        print(luckynum)
        for pos in luckynumpos:
            print(f'Vi tri [{pos[0]}][{pos[1]}]')
        
main()