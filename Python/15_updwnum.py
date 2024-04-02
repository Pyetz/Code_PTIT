def check_updwnum(num):
    if len(num) < 3:
        return False
    highest = False
    for i in range(len(num) - 1):
        if num[i+1] == num[i]:
            return False
        elif num[i+1] > num[i]:
            if highest == True:
                return False
            continue
        else:
            highest = True
            continue
    return True

def input_testcases(tess):
    test_cases = []
    for i in range(tess):
        test_cases.append(input())

    return test_cases

def main():
    tess = int(input())
    test_cases = input_testcases(tess)

    for num in test_cases:
        if check_updwnum(num):
            print("YES")
        else:
            print("NO")

main()