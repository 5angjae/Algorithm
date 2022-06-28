import sys


def calc(notation):
    l = len(notation)
    stack = []
    for i in range(l):
        if notation[i] == "+":
            y = stack.pop()
            x = stack.pop()
            stack.append(x+y)

        elif notation[i] == "-":
            y = stack.pop()
            x = stack.pop()
            stack.append(x - y)

        elif notation[i] == "*":
            y = stack.pop()
            x = stack.pop()
            stack.append(x * y)

        elif notation[i] == "/":
            y = stack.pop()
            x = stack.pop()
            stack.append(x / y)

        else:
            stack.append(numbers[notation[i]])

    return stack.pop()

N = int(input())
postfix_notation = input()

numbers = {}

# chr(65) = A
start_ascii = 65
for i in range(N):
    numbers[chr(start_ascii + i)] = int(input())

print("{:.2f}".format(calc(postfix_notation)))