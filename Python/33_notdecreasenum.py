def not_decrease_num(n):
    if len(n) == 1:
        return False
    current = n[0]
    for i in n:
        if i < current:
            return False
        current = i
    return True

def read_bin_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return data

def not_decrease_num_sequence(data1, data2):
    data1 = [int(i) for i in data1]
    data2 = [int(i) for i in data2]
    result = list(set(data1 + data2))
    result = [i for i in result if not_decrease_num(str(i))]
    return sorted(result)

def main():
    data1 = read_bin_file('DATA1.in')
    data2 = read_bin_file('DATA2.in')

    sequence = not_decrease_num_sequence(data1, data2)

    for i in sequence:
        print(f'{i} {data1.count(i)} {data2.count(i)}')

main()
