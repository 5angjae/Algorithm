# 백준 17609 회문
def palindrome(text):
    length = len(text)
    result = 0
    for i in range(length//2):
        if text[i] != text[length-i-1]:
            result = 1
            break

    return result


tc = int(input())

for _ in range(tc):
    text = input()

    if palindrome(text) == 0:
        print(0)
    else:
