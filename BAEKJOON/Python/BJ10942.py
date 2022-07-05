import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
P = [[0] * N for _ in range(N)]
for i in range(N):
    P[i][i] = 1

for i in range(N - 1):
    if numbers[i] == numbers[i + 1]:
        P[i][i + 1] = 1

for i in range(2, N):
    for j in range(N - i):
        if numbers[j] == numbers[j + i] and P[j + 1][j + i - 1] == 1:
            P[j][i + j] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(P[S - 1][E - 1])