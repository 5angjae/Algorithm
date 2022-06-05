# BJ 1720 - 타일 코드
# n = 1 : 1
# n = 2 : 3
# n = 3 : 5 / 1*2 + 3

N = int(input())
All = [0] * 31
Sym = [0] * 31
All[1] = 1
All[2] = 3
Sym[1] = 1
Sym[2] = 3
Sym[3] = 1
Sym[4] = 5

# 대칭 신경 안쓴 경우의 수
for i in range(3, N+1):
    All[i] = 2 * All[i-2] + All[i-1]

# 대칭인 경우의 수
for i in range(5, N+1):
    Sym[i] = 2 * Sym[i-4] + Sym[i-2]

# 대칭 신경 쓴 경우의 수
print((All[N] - Sym[N])//2 + Sym[N])