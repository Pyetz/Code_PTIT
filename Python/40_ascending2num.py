def ascending_2num_in_sequence(sequence):
    result = []
    for i in range(0, len(sequence) - 1, 2):
        num = int(sequence[i] + sequence[i + 1])
        if num not in result:
            result.append(num)

    return sorted(result)

def main():
    sequence = input()
    print(' '.join(map(str, ascending_2num_in_sequence(sequence))))

main()