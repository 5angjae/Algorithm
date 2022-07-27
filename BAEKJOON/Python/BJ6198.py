# BOJ 6198 옥상정원꾸미기
N = int(input())
heights = [int(input()) for _ in range(N)]
# 자기보다 큰 건물 나오기 전까지 개수
# 자신 왼쪽 건물 중, 자신을 볼 수 있는 건물 수.
stack = []
answer = 0

for i in range(N):
    while stack and stack[-1] <= heights[i]: # 왼쪽의 건물이 더 작거나 같으면 빼면 됨
        stack.pop()
    answer += len(stack)
    stack.append(heights[i])

print(answer)