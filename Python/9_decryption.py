def input_test_cases(tess):
    test_cases = []
    for i in range(tess):
        test_cases.append(input())
    return test_cases

def decryption(test_cases):
    for case in test_cases:
        result = ''
        for i in range(0, len(case), 2):
            result += case[i] * int(case[i+1])
        print(result)

def main():
    tess = int(input())
    test_cases = input_test_cases(tess)

    decryption(test_cases)

main()