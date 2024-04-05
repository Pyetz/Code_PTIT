def sort_product(lst_num):
    lst_product_digits = []
    for num in lst_num:
        product_digits = 1
        for digit in num:
            product_digits *= int(digit)
        lst_product_digits.append(product_digits)
    lst_num = [int(num) for num in lst_num]

    result = []
    while lst_product_digits:
        min_val = min(lst_product_digits)
        lst_current_min = []
        while min_val in lst_product_digits:
            index_min = lst_product_digits.index(min_val)
            lst_current_min.append(lst_num[index_min])
            lst_product_digits.pop(index_min)
            lst_num.pop(index_min)
        lst_current_min.sort()
        result.extend(lst_current_min)

    return ' '.join([str(num) for num in result])

def input_testcases(tess):
    testcases = []
    for _ in range(tess):
        tess = int(input())
        lst_num = input().split()
        lst_num = [lst_num[i] for i in range(tess)]
        testcases.append(lst_num)
    return testcases


def main():
    tess = int(input())
    test_cases = input_testcases(tess)

    for test_case in test_cases:
        print(sort_product(test_case))
    

main()