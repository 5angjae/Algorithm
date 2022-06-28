# 백준 1563 개근상
import sys
input = sys.stdin.readline

N = int(input())

# 지각 2번 이상 or 결석 3번 연속
# 출석 지각 결석
# n = 1 -> 1 1 1 3
# n = 2 -> 3 2 3 8
# 개근상 o[n] = 3*o[n-1] - l[n-1] - aa[n-1]
# 1번 지각한 경우 l[n] = l[n-1] * 2 + (o[n-1] - l[n-1])
# aa[n] = a[n-1]
# a[n] = o[n-1] - a[n-1]

a = [0] * (N+1)
aa = [0] * (N+1)
l = [0] * (N+1)
o = [0] * (N+1)

a[1] = 1
o[1] = 3
l[1] = 1

for i in range(2, N+1):
    a[i] = o[i-1] - a[i-1]
    aa[i] = a[i-1]
    l[i] = o[i-1] + l[i-1]
    o[i] = 3*o[i-1] - l[i-1] - aa[i-1]

    a[i] %= 1000000
    aa[i] %= 1000000
    l[i] %= 1000000
    o[i] %= 1000000

print(o[N])