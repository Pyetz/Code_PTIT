def is_lucky(num):
    return str(num).count("4") + str(num).count("7") in [4, 7]

def main():
    N = int(input())

    if is_lucky(N):
        print("YES")
    else:
        print("NO")
    
main()