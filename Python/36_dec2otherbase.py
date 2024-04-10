def base_format(num):
    base_36_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return base_36_digits[num]

def dec2otherbase(num, base):
    result = ''
    while num > 0:
        result = base_format(num % base) + result
        num = num // base
    return result

def input_testcases(tess):
    testcases = []
    for _ in range(tess):
        testcases.append(tuple(map(int, input().split())))
    return testcases

def main():
    tess = int(input())
    test_cases = input_testcases(tess)

    for case in test_cases:
        num, base = case
        print(dec2otherbase(num, base))

main()
