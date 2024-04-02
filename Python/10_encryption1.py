def input_test_cases(tess):
    test_cases = []
    for i in range(tess):
        test_cases.append(input())
    return test_cases

def encryption(test_cases):
    for case in test_cases:
        result = ''
        current_letter = case[0]
        count = 0
        for i in case:
            if i == current_letter:
                count += 1
            else:
                result += str(count) + current_letter
                current_letter = i
                count = 1
        result += str(count) + current_letter
            
        print(result)

def main():
    tess = int(input())
    test_cases = input_test_cases(tess)

    encryption(test_cases)

main()