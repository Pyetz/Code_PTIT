def add_comma(N):
    for i in range(len(N)-3, -1, -3):
        N = N[:i] + ',' + N[i:]
    if N[0] == ',':
        N = N[1:]
    print(N)

def main():
    N = input()

    add_comma(N)

main()