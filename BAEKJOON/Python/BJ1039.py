from itertools import combinations
from collections import deque
import copy

def BFS():
    check = []
    max_num = 0
    len_queue = len(queue)
    while len_queue > 0:
        x = queue.popleft()
        list_x = list(x)
        
        # print(list_x)
        for i, j in comb:
            list_nx = copy.deepcopy(list_x)
            list_nx[i], list_nx[j] = list_nx[j], list_nx[i]
            
            if list_nx[0] == '0':
                continue
            nx = int("".join(list_nx))
            if nx not in check:
                # print(nx)
                check.append(nx)
                queue.append(str(nx))
                max_num = max(max_num, nx)
        len_queue -= 1
    return max_num

N, K = map(str, input().split())
comb = list(combinations(range(len(N)), 2))
# print(comb)
answer = ""
queue = deque()
queue.append(N)
K = int(K)
while K > 0:
    answer = BFS()
    K -= 1

if not answer:
    print(-1)
else:
    print(answer)


# # 문제점 : 애초에 최대인 경우일 때는 안바꿔준다.

# N, K = map(str, input().split())
# M = len(N)
# K = int(K)
# if K > (M*(M-1)//2):
#     print(-1)
# else:
#     arr = []
#     for _ in range(K):
#         max_N = 0
#         max_idx = 0
#         for i in range(len(N)):
#             if int(N[i]) >= max_N:
#                 max_N = int(N[i])
#                 max_idx = i
#         arr.append(N[max_idx])
#         temp = N[1:max_idx] + N[0]
#         if max_idx < len(N) - 1:
#             temp += N[max_idx+1:]
#         N = temp
    
# answer = ""
# for a in arr:
#     answer += a
# answer += N
# print(answer)