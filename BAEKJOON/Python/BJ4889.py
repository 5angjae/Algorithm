from collections import deque

tc = 1
while True:
    input_text = input()
    if "-" in input_text:
        break

    answer = 0

    stack = []


    for t in input_text:
        if t == "{":
            stack.append(t)
        elif t == "}" and stack and stack[-1] == "{":
            stack.pop()
        else:
            stack.append(t)

    queue = deque(stack)
    cnt = 0
    new_stack = []
    while queue:
        q = queue.popleft()
        if q == "}":
            if len(new_stack) == 0:
                new_stack.append("{")
                cnt += 1
            else:
                new_stack.pop()
        else:
            if len(new_stack) == 0:
                new_stack.append("{")
            else:
                new_stack.pop()
                cnt += 1


    print(str(tc) + ".", cnt)
    tc += 1