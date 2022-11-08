# BAEKJOON 18353 병사 배치하기

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

# 작아지는 수열을 만들어야 하니까
# 뒤에 위치할 값보다 큰 값들의 수를 세야 한다.
#
for i in range(N):
    #print(i)
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)

print(N - max(dp))
# 15 11 4 8 5 2 4
# 1 1 1 1 1 1 1
#