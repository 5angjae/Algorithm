# BOJ 1449 수리공 항승

def tape(x):
    for i in range(x, x+L):
        cover.append(i)

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cover = []
cnt = 0

for a in arr:
    if a not in cover:
        tape(a)
        cnt += 1
    else:
        pass

print(cnt)