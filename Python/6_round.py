def round_float(num):
    dot_index = str(num).find('.')
    if num[dot_index+1] >= '5':
        return str(int(num[:dot_index])+1)
    else:
        return num[:dot_index]

def round_num(num):
    if int(num) <= 10:
        return num
    else:
        result = ''
        round_num = num
        for _ in range(0, len(num) - 2):
            round_num = round_float(round_num[:-1] + '.' + round_num[-1])
            result += '0'
        result = round_float(round_num[:-1] + '.' + round_num[-1]) + '0' + result
        
        
        return result

def input_test_cases(test_num):
    test_cases = []
    for _ in range(test_num):
        test_cases.append(input())
    return test_cases

def main():
    test_num = int(input())
    test_cases = input_test_cases(test_num)

    for case in test_cases:
        print(round_num(case))
    
main()