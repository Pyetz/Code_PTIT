def sieve_of_eratosthenes(n = 1000001):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def is_symmetric(n):
    return str(n) == str(n)[::-1]

def input_test_cases(test_num):
    test_cases = []
    for i in range(test_num):
        test_cases.append(int(input()))
    return test_cases

def print_emirp(primes, test_cases):
    for case in test_cases:
        result = ""
        first = True
        for i in range(case):
            if i in primes and not is_symmetric(i):
                if first:
                    result += str(i)
                    first = False
                else:
                    result += " " + str(i)
        print(result)

def main():
    test_num = int(input())
    test_cases = input_test_cases(test_num)
    primes = sieve_of_eratosthenes(max(test_cases) + 1)

    print_emirp(primes, test_cases)
    
main()

    