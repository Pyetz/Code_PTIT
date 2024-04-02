def input_test_cases():
    test_cases = []
    test_cases.append(input())
    while test_cases[-1] != '0':
        test_cases.append(input())
    test_cases.pop()
    return test_cases

def encryption(test_cases):
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    for case in test_cases:
        result = ''
        index = 0
        K = ''
        while not case[index] == " ":
            K += case[index]
            index += 1

        K = int(K)

        for i in case[index+1:]: 
            result += P[(P.index(i) + K) % 28]
            
        print(result)

def main():
    test_cases = input_test_cases()

    encryption(test_cases)

main()