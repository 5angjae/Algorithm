text = input()

if text == "P" or text == "PPAP":
    print("PPAP")
else:
    stack = []
    for i in text:
        stack.append(i)
        if stack[-4:] == ["P", "P", "A", "P"]:
            for j in range(3):
                stack.pop()

    if stack == ["P", "P", "A", "P"] or stack == ["P"]:
        print("PPAP")
    else:
        print("NP")