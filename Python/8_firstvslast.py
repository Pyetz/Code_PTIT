def is_2first_2last(num):
    return num[0:2] == num[-2:]

def input_test_cases(tess):
    test_cases = []
    for i in range(tess):
        test_cases.append(input())
    return test_cases

def print_result(test_cases):
    for case in test_cases:
        if is_2first_2last(case):
            print('YES')
        else:
            print('NO')

def main():
    tess = int(input())
    test_cases = input_test_cases(tess)

    print_result(test_cases)

main()