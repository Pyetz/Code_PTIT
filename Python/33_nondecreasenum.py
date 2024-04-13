def non_decreasing_num(n):
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
    return tuple(data)

def non_decrease_num_sequence(data1, data2):
    result = set(data1).union(data2)
    for i in result:
        if not non_decreasing_num(i):
            result.remove(i)
    return sorted(result)

def main():
    data1, data2 = read_bin_file('DATA1.in'), read_bin_file('DATA2.in')
    sequence = non_decrease_num_sequence(data1, data2)

    for i in sequence:
        print(i, data1.count(i), data2.count(i))

main()
