def process(s):
    maxVal = ""
    tempStr = ""

    for i in range(len(s)-1):
        if s[i].isdecimal() == False:
            if tempStr != "":
                if (maxVal == "" or int(tempStr) > int(maxVal)):
                    maxVal = tempStr
                tempStr = ""
            continue
        else:
            tempStr += s[i]

    if s[-1].isdecimal():
        tempStr += s[len(s)-1]
        if (maxVal == "" or int(tempStr) > int(maxVal)):
            maxVal = tempStr

    return maxVal

def input_testcases(tess):
    test_cases = []
    for i in range(tess):
        test_cases.append(input())
    return test_cases

def main ():
    tess = int(input())
    test_cases = input_testcases(tess)
    for i in range(tess):
        print(process(test_cases[i]))

main()
