def parentheses_pos(expression):
    current_open = 0
    current_close = []
    appearance_order = []
    for char in expression:
        if char == '(':
            current_open += 1
            current_close.append(current_open)
            appearance_order.append(current_open)
        elif char == ')':
            appearance_order.append(current_close[-1])
            current_close.pop()

    return appearance_order

def main():
    tess = int(input())
    test_cases = [input() for _ in range (tess)]

    for case in test_cases:
        appearance_order = parentheses_pos(case)
        print(' '.join(map(str, appearance_order)))

main()