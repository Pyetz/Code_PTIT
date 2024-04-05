def is_python_file(S):
    return S.lower().endswith('.py')

def main():
    S = input()
    if is_python_file(S):
        print("yes")
    else:
        print("no")

main()