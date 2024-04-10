def find_min_group (sequence, K):
    min_group = 1
    for i in range(len(sequence) - 1):
        if sequence[i + 1] - sequence[i] > K:
            min_group += 1

    return min_group

def input_sequence(tess):
    testcases = map(int, input().split())
    return sorted(list(testcases))

def main():
    tess, K = map(int, input().split())
    sequence = input_sequence(tess)

    print(find_min_group(sequence, K))

main()
    