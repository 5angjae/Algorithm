test_case = int(input())

for _ in range(test_case):
    input_text = input()
    cursor_left = []
    cursor_right = []

    for t in input_text:
        if t == '<':
            if cursor_left:
                cursor_right.append(cursor_left.pop())
        elif t == '>':
            if cursor_right:
                cursor_left.append(cursor_right.pop())
        elif t == '-':
            if cursor_left:
                cursor_left.pop()
        else:
            cursor_left.append(t)

    cursor_left.extend(reversed(cursor_right))
    print(''.join(cursor_left))