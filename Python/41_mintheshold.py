def nums_in_sequence(sequence):
    result = []
    for i in range(0, len(sequence) - 1, 2):
        num = int(sequence[i] + sequence[i + 1])
        if num not in [x[0] for x in result]:
            result.append([num, 1])
        else:
            for x in result:
                if x[0] == num:
                    x[1] += 1

    return sorted(result, key=lambda x: x[0])

def main():
    sequence = input()
    min_threshold = int(input())
    nums = nums_in_sequence(sequence)

    found = False
    for num in nums:
        if num[1] >= min_threshold:
            found = True
            print(num[0], num[1])

    if not found:
        print("NOT FOUND")
main()