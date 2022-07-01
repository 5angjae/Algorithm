from collections import deque

N, M = map(int, input().split())
books = list(map(int, input().split()))
dists = []

books.sort()
books = deque(books)

while books:
    state = 0
    if abs(books[0]) > abs(books[-1]):
        dists.append(abs(books[0]))
        
        if books[0] < 0:
            state = -1
        for i in range(M):
            if state == -1:
                
                if books[0] < 0:
                    books.popleft()
                else:
                    break
            
            if len(books) == 0:
                break
    elif abs(books[0]) < abs(books[-1]):
        dists.append(abs(books[-1]))
        if books[-1] > 0:
            state = 1
        for i in range(M):
            if state == 1:
                if books[-1] > 0:
                    books.pop()
                else:
                    break
            if len(books) == 0:
                break
    else:
        dists.append(abs(books[0]))
        while books:
            books.pop()

            
answer = 0
for dist in dists:
    answer += (2*dist)
answer -= max(dists)
print(answer)
# books.sort()

# books = deque(books)
# while books:
#     if abs(books[0])>abs(books[-1]):
#         dists.append(abs(books[0])
#         for i in range(M):
#             books.popleft()
#             if len(books) == 0:
#                 break
#     else:
#         dists.append(abs(books[-1]))
#         for i in range(M):
#             books.pop()
#             if len(books) == 0:
#                 break
# dists.sort()
# print(dists)
# answer = 0
# for dist in dists:
#     answer += (2 * dist)
# answer -= dist[-1]
# print(answer)