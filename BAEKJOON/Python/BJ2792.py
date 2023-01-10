import sys

input = sys.stdin.readline

N, M = map(int, input().split())
colors = []
max_color = 0
for _ in range(M):
    color = int(input())
    colors.append(color)
    max_color = max(max_color, color)

answer = max_color
# 이분탐색

left = 1
right = max_color

while left <= right:
    mid = (left+right)//2

    # mid 개 씩 나눠줬을때 필요한 사람 수
    p = 0
    for color in colors:
        p += color // mid
        if color % mid > 0:
            p += 1

    if p > N:
        left = mid + 1
    else:
        answer = min(answer, mid)
        right = mid - 1

print(answer)