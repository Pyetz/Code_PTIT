def round_num(num):
    if num <= 10:
        return num
    else:
        result = ""
        current_idx = -1
        while num[current_idx] != num[0]:
            if int(num[current_idx]) >= 5:
                num[current_idx-1] = str(int(num[current_idx-1]) + 1)
            result += "0"
            current_idx -= 1

        result += num[0]
        return result

def input_test_cases(test_num):
    test_cases = []
    for _ in range(test_num):
        test_cases.append(int(input()))
    return test_cases

def print_rounded(test_cases):
    for case in test_cases:
        print(round_num(case))

def main():
    test_num = int(input())
    test_cases = input_test_cases(test_num)

    print_rounded(test_cases)
    
main()