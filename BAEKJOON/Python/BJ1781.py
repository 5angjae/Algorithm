# BJ 1781 컵라면
import heapq # min heap
import sys
input = sys.stdin.readline

N = int(input())

prob_info = [list(map(int, input().split())) for _ in range(N)]

prob_info.sort() # 가중치 순서대로 정렬

queue = []

for i in prob_info: # 가중치 순서대로 돌면서 해당 가중치 초 때 바꺼 넣을 수 잇는지 확인
    heapq.heappush(queue, i[1]) # 일단 넣고
    if i[0] < len(queue):
        heapq.heappop(queue) # min heap에서 하나를 뺀다. (최소)

print(sum(queue))