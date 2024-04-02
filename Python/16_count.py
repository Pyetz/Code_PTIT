def check(num):
    if len(num) <= 1:
        return False
    return num == num[::-1]

def input_testcases(tess):
    test_cases = []
    for i in range(tess):
        test_cases.append(input())

    return test_cases

def sum_digits(num):
    sum_digit = 0
    for digit in num:
        sum_digit += int(digit)

    return str(sum_digit)

def main():
    tess = int(input())
    test_cases = input_testcases(tess)

    for num in test_cases:
        sum_digits_in_num = sum_digits(num)
        if check(sum_digits_in_num):
            print("YES")
        else:
            print("NO")

main()