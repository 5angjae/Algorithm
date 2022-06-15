# 백준 2302 극장좌석
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
fixed = [0] * (M + 2)
fixed[0] = 0
for i in range(1, M+1):
    fixed[i] = int(input())
fixed[M+1] = N+1
# 구간 길이 1 ~ fixed[0]
# 총 연결 구간에서 가능한 경우의수를 각각 구해서 곱하기
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[n] = dp[n-1] + dp[n-2]

# 구간 길이 배열 len
len = []
for i in range(M+1):
    len.append(fixed[i+1] - fixed[i] - 1)

dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, N+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
for l in len:
    answer *= dp[l]

print(answer)