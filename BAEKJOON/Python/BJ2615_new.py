# 오목 2615번
import sys
arr = [list(map(int, input().split())) for _ in range(19)]

dx = [1, 0, 1, 1]
dy = [0, 1, 1, -1]

for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            winner = arr[i][j]

            for d in range(4):
                cnt = 1
                ni = i + dy[d]
                nj = j + dx[d]

                while 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == winner:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= i - dy[d] < 19 and 0 <= j - dx[d] < 19 and arr[i-dy[d]][j-dx[d]] == winner:
                            break
                        if 0 <= ni + dy[d] < 19 and 0 <= nj + dx[d] < 19 and arr[ni+dy[d]][nj+dx[d]] == winner:
                            break
                        print(winner)
                        print(i+1, j+1)
                        sys.exit(0) # 프로그램을 종료 시켜서 반복문을 끝냄
                    ni += dy[d]
                    nj += dx[d]

print(0)