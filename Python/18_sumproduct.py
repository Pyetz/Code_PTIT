
def sum_product(num):
    sum_odd = sum([int(i) for i in num[::2]])
    product_even = 1
    is_all_zero = all(i == "0" for i in num[1::2])
    if is_all_zero:
        return sum_odd, 0
    for i in num[1::2]:
        if i != "0":
            product_even *= int(i)
    return str(sum_odd), str(product_even)

def main():
    test_num = int(input())
    test_cases = [input() for _ in range(test_num)]

    for case in test_cases:
        sum_even, product_odd = sum_product(case)
        print(sum_even, product_odd)
    
main()