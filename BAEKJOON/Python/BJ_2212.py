import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
points = list(map(int, input().split()))
points.sort()
# K-1개 구분 선

if K >= N:
    print(0)
    sys.exit()

dist = []
for i in range(1, N):
    dist.append(points[i] - points[i-1])

dist.sort(reverse=True)

for _ in range(K-1):
    dist.pop(0)

print(sum(dist))