def limit():
    result = 0
    for i in range(32):
        result += 2**i
    lower_bound = (-result // 2)
    upper_bound = (result // 2)

    return lower_bound, upper_bound

def find_non_ints(data):
    lines = data.split('\n')
    lower_bound, upper_bound = limit()
    result = []

    for line in lines:
        line = line.split()
        for element in line:
            if element.isdecimal():
                if not (lower_bound <= int(element) <= upper_bound):
                    result.append(element)
            else:
                result.append(element)

    return sorted(result)

def main():
    with open('DATA.in', 'rb') as file:
        data = file.read().decode('utf-8')

    non_int_lst = find_non_ints(data)

    for element in non_int_lst:
        print(element, end=' ')

main()