# BOJ12847 꿀 아르바이트
# 구간합, 슬라이딩 윈도우
n, m = map(int, input().split())
T = list(map(int, input().split()))

# 구간합
part_sum = [0] * (n+1)
sum = 0
for i in range(1,n+1):
    sum += T[i-1]
    part_sum[i] = sum
#print(part_sum)
max_T = 0
for i in range(1, n-m+1):
    if (part_sum[m+i-1] - part_sum[i-1]) > max_T:
        max_T = (part_sum[m+i-1] - part_sum[i-1])
        #print(max_T)

print(max_T)