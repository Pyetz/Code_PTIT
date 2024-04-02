import math

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def input_testcases(tess):
    test_cases = []
    for _ in range(0, tess):
        test_cases.append(input())

    return test_cases

def check_primepos(num):
    for i in range(len(num)):
        if (check_prime(int(num[i])) and (not check_prime(i))) or (not check_prime(int(num[i])) and check_prime(i)):
            return False
    return True

def main():
    tess = int(input())
    test_cases = input_testcases(tess)

    for num in test_cases:
        if check_primepos(num):
            print("YES")
        else:
            print("NO")

main()