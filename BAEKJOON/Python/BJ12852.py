# BOJ 12852 1로 만들기 2

N = int(input())
# n = 1 -> 0
# n = 2 -> 1
# n = 3 -> 1
# n = 4 -> 2
# n = 5 -> 3

cal = [0] * (10**6 + 1)
cal[1] = 0
cal[2] = 1
cal[3] = 1
cal[4] = 2

for i in range(5, N+1):
    a = 10 ** 6
    b = 10 ** 6
    c = 10 ** 6
    if i % 3 == 0:
        a = cal[i//3] + 1
    if i % 2 == 0:
        b = cal[i//2] + 1
    c = cal[i-1] + 1
    cal[i] = min(a, b, c)
print(cal[N])

process = []
while N > 1:
    process.append(N)
    if cal[N] - 1 == cal[N // 3] and N % 3 == 0:
        N //= 3
    elif cal[N] - 1 == cal[N // 2] and N % 2 == 0:
        N //= 2
    elif cal[N] - 1 == cal[N - 1]:
        N -= 1
process.append(1)
print(" ".join(map(str, process)))