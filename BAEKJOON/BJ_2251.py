from collections import deque

def visit_check(x, y):
    if visited[x][y] == 0:
        visited[x][y] = 1
        q.append((x,y))

A, B, C = map(int, input().split())

answer = []

# https://velog.io/@gyhan/Python-Deque.popleft%EB%8A%94-%EC%99%9C-%EB%B9%A0%EB%A5%B8%EA%B0%80
# list.pop(0) VS deque.popleft()
# list.pop(0)의 경우, 맨앞을 빼주고 모든 데이터를 조회해서 한칸씩 앞으로 옮겨주는 작업 필요 O(n)
# deque.popleft()의 경우, rear와 front를 가리키는 변수를 내부에 가지고 있어 해당 포인터 조정을 통해 앞 뒤에서 모두 삽입이 가능한 구조 O(1)

q = deque()
q.append((0,0))

# A 물통의 양 : x
# B 물통의 양 : y
# C 물통의 양 : z = C-x-y
# 2개만 정해지면 나머지는 자동으로 정해지기 때문에 x, y에 대해서만 방문기록을 남겨 같은 상황을 반복하지 않도록 한다.
visited = [[0] * (B+1) for _ in range(A+1)]
visited[0][0] = 1

while q:
    x, y = q.popleft()
    z = C-x-y

    if x == 0:
        answer.append(z)

    # A -> B
    water = min(x, B-y)
    visit_check(x-water, y+water)
    # A -> C
    water = min(x, C-z)
    visit_check(x-water, y)
    # B -> A
    water = min(y, A-x)
    visit_check(x+water, y-water)
    # B -> C
    water = min(y, C-z)
    visit_check(x,y-water)
    # C -> A
    water = min(z, A-x)
    visit_check(x+water,y)
    # C -> B
    water = min(z, B-y)
    visit_check(x,y+water)


answer.sort()
for i in answer:
    print(i, end=" ")