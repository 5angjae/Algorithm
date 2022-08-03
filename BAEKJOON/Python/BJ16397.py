# 탈출
from collections import deque

def click_A(N):
    return N+1

def click_B(N):
    if N == 0:
        return N
    else:
        temp = 2 * N
        if temp > 99999:
            return -1
        elif 0 < temp // 10000 < 10:
            answer = temp - 10000
        elif 0 < temp // 1000 < 10:
            answer = temp - 1000
        elif 0 < temp // 100 < 10:
            answer = temp - 100
        elif 0 < temp // 10 < 10:
            answer = temp - 10
        elif 0 < temp < 10:
            answer = temp - 1
        return answer


N, T, G = map(int, input().split())
check = [0] * 100000
q = deque()
q.append([N, 0])
check[N] = 1
minanswer = T + 1
while q:
    x, cnt = q.popleft()
    if cnt > T:
        break
    if x == G:
        if minanswer > cnt:
            minanswer = cnt
        continue
    nx = click_A(x)
    if 0 <= nx <= 99999:
        if check[nx] == 0:
            q.append([nx, cnt+1])
            check[nx] = 1
    nx = click_B(x)
    if 0 <= nx <= 99999:
        if check[nx] == 0:
            q.append([nx, cnt + 1])
            check[nx] = 1

if minanswer == T+1:
    print("ANG")
else:
    print(minanswer)