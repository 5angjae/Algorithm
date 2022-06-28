# 오목 2615번
# 이렇게 가면 특정 경우에서는 격자의 범위를 벗어나게 되는 경우가 생기고 그 경우에서는 에러가 날 수 있다.
# 새로운 방법으로 다시 풀이하자.
def find_winner(i, j):
    dx = [1, 0, 1, -1]
    dy = [0, 1, 1, 1]
    for i in range(4):
        # arr[i][j] , arr[i + dy][j + dx] , arr[i + 2*dy][j + 2*dx] , arr[i + 3*dy][j + 3*dx] , arr[i + 4*dy][j + 4*dx] , arr[i + 5*dy][j + 5*dx]
        if arr[i][j] == arr[i + dy[i]][j + dx[i]] and arr[i][j] == arr[i + 2*dy[i]][j + 2*dx[i]] and arr[i][j] == arr[i + 3*dy[i]][j + 3*dx[i]] and arr[i][j] == arr[i + 4*dy[i]][j + 4*dx[i]]:
            if arr[i][j] == arr[i + 5*dy[i]][j + 5*dx[i]]:
                pass
            else:
                visited[i][j] = 1
                visited[i + dy[i]][j + dx[i]] = 1
                visited[i + 2 * dy[i]][j + 2 * dx[i]] = 1
                visited[i + 3 * dy[i]][j + 3 * dx[i]] = 1
                visited[i + 4 * dy[i]][j + 4 * dx[i]] = 1
                return i

    return -1

arr = [list(map(int, input().split())) for _ in range(19)]
# 오른쪽, 아래, 오른쪽아래 대각, 왼쪽 아래 대각


visited = [[0] * 19 for _ in range(19)]
result = 0
result_dir = -1
for i in range(19):
    for j in range(19):
        if arr[i][j] != 0 and visited[i][j] == 0 and find_winner(i, j) != -1:
            result = arr[i][j]
            result_dir = find_winner(i, j)
            break
    if result != 0:
        break

print(result)
if result_dir == 3:
    print(i+5, j-3)
elif result_dir == -1:
    pass
else:
    print(i+1, j+1)