def include_9_divisor(num):
    count = 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            if i*i != num:
                count += 2
            else:
                count += 1
            if count > 7:
                return False
    if count == 7:
        return True
    return False
def main():
    # num = int(input())
    num = 1000000
    count = 0
    for i in range(1, num+1):
        if include_9_divisor(i):
            count += 1

    print(count)


main()