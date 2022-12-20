N, M = map(int, input().split())

times = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if times[i][j] > times[i][k] + times[k][j]:
                times[i][j] = times[i][k] + times[k][j]


for _ in range(M):
    A, B, C = map(int, input().split())

    if times[A-1][B-1] <= C:
        print("Enjoy other party")
    else:
        print("Stay here")


# 125,000,000