# BJ1303 전쟁 - 전투
N, M = map(int, input().split())
# 81 + 49 / 1+64

soldiers = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

