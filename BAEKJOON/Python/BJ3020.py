# BAEKJOON 3020 개똥벌레
import sys
input = sys.stdin.readline

N, H = map(int, input().split())
arr = [0] * H

# 저번에 그거네
for i in range(N):
    high = int(input())
    if i%2 == 0:
        arr[H-high] += 1
    else:
        arr[0] += 1
        arr[high] -= 1

for i in range(1, H):
    arr[i] += arr[i-1]

cnt = 0
low = min(arr)
for i in arr:
    if i == low:
        cnt += 1

print(low, cnt)

# for i in range(N):
#     temp = int(input())
#     if i % 2 == 0:
#         for j in range(temp):
#             answer[j] += 1
#     else:
#         for j in range(H-1, H-temp-1, -1):
#             answer[j] += 1
#
# min_cnt = N
# cnt = 0
# # for a in arr:
# #     if a.count(1) < max_cnt:
# #         cnt = 1
# #         max_cnt = a.count(1)
# #     elif a.count(1) == max_cnt:
# #         cnt += 1
#
# for a in answer:
#     if a < min_cnt:
#         cnt = 1
#         min_cnt = a
#     elif a == min_cnt:
#         cnt += 1
#
# print(min_cnt, cnt)
# #100,000,000,000
