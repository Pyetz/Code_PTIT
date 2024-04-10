def bin2oct(num):
    num = '0' * (3-len(num)%3) + num
    octal = ''
    for i in range(0, len(num), 3):
        octal += str(int(num[i]) * 4 + int(num[i+1]) * 2 + int(num[i+2]))
    return int(octal)

def main():
    num = input()
    print(bin2oct(num))
    
main()