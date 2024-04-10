def intersection(A, B):
    return set(A).intersection(B)

def subtraction(A, B):
    return set(A).difference(B)

def process_input():
    lenA, lenB = map(int, input().split())
    A_input = map(int, input().split())
    A_input = list(A_input)
    A = []
    for i in range(lenA):
        if A_input[i] not in A:
            A.append(A_input[i])
    B_input = map(int, input().split())
    B_input = list(B_input)
    B = []
    for i in range(lenB):
        if B_input[i] not in B:
            B.append(B_input[i])
    return A, B

def main():
    A, B = process_input()
    print(' '.join(map(str, sorted(intersection(A, B)))))
    print(' '.join(map(str, sorted(subtraction(A, B)))))
    print(' '.join(map(str, sorted(subtraction(B, A)))))

main()