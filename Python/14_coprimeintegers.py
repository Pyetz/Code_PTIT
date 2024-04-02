def gcd (a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def check_coprime(num):
    num_reverse = int(str(num)[::-1])
    return gcd(num, num_reverse) == 1

def input_test_cases(test_num):
    test_cases = []
    for _ in range(test_num):
        test_cases.append(int(input()))
    return test_cases

def main():
    tess = int(input())
    test_cases = input_test_cases(tess)

    for case in test_cases:
        if check_coprime(case):
            print("YES")
        else:
            print("NO")

main()
