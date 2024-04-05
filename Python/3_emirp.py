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

def emirp_lst(primes, case):
    prime_set = set(primes)
    result = ""
    for prime in primes:
        reversed_prime = int(str(prime)[::-1])
        if reversed_prime > case:
            break
        if prime not in prime_set:
            continue
        if reversed_prime in prime_set:
            if not is_symmetric(prime) and not is_symmetric(reversed_prime):
                result += str(prime) + " " + str(reversed_prime)+ " "
                prime_set.remove(reversed_prime)

    return result.strip()

def main():
    test_num = int(input())
    test_cases = [int(input()) for _ in range(test_num)]
    max_case = max(test_cases)
    primes = sieve_of_eratosthenes(max_case)

    for case in test_cases:
        print(emirp_lst(primes, case))
    
main()