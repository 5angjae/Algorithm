# BOJ 2467 용액
import sys

N = int(input())
arr = list(map(int, input().split()))

x = 0
y = N-1
nearest_diff = sys.maxsize
nearest_x = 0
nearest_y = 0
while x < y:
    # print("반복문",x, y)
    diff = arr[x] + arr[y]
    diff_abs = abs(diff)
    if diff_abs < nearest_diff:
        nearest_diff = diff_abs
        nearest_x = x
        nearest_y = y

    if diff > 0:
        y -= 1
    elif diff < 0:
        x += 1
    else:
        break

print(arr[nearest_x], arr[nearest_y])