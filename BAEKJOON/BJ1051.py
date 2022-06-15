import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [list(input())[:M] for _ in range(N)]

# N, M 중 작은 숫자부터 찾아 나가면 되지 않나 싶다.
start = min(N, M)
while start > 1:
    state = 0
    for i in range(N-start+1):
        for j in range(M-start+1):
            if numbers[i][j] == numbers[i][j+start-1] and numbers[i][j] == numbers[i+start-1][j] and numbers[i][j] == numbers[i+start-1][j+start-1]:
                state = 1
                break
        if state == 1:
            break
    if state == 1:
        break
    else:
        start -= 1

print(start ** 2)
