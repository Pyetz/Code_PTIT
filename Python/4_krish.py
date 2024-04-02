def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num+1):
        result *= i
    return result

def is_krish(num):
    num = str(num)
    result = 0
    for i in num:
        result += factorial(int(i))
    return result == int(num)

def input_test_cases(test_num):
    test_cases = []
    for _ in range(test_num):
        test_cases.append(int(input()))
    return test_cases

def print_krish(test_cases):
    for case in test_cases:
        print("Yes" if is_krish(case) else "No")

def main():
    test_num = int(input())
    test_cases = input_test_cases(test_num)

    print_krish(test_cases)

main()
