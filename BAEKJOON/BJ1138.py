# 백준 1138번 한줄로 서기
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = [0] * N

for i in range(N):
    if answer[arr[i]] == 0:
        answer[arr[i]] = i+1
    else:
        index = arr[i]
        while True:
            index += 1
            cnt = 0
            for j in range(index):
                if answer[j] == 0:
                    cnt += 1
            if cnt == arr[i] and answer[index] == 0:
                break

        answer[index] = i+1

for i in range(N):
    answer[i] = str(answer[i])

print(" ".join(answer))
