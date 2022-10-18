# BOJ 1969 DNA

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
answer = ""
HD = 0
# 각 자리별 가장 많은거로 만들면 될 듯
for i in range(M):
    RNA = [0,0,0,0] # A C G T 순서 개수
    for j in range(N):
        if arr[j][i] == "A":
            RNA[0] += 1
        elif arr[j][i] == "C":
            RNA[1] += 1
        elif arr[j][i] == "G":
            RNA[2] += 1
        elif arr[j][i] == "T":
            RNA[3] += 1
    idx = RNA.index(max(RNA))
    if idx == 0:
        answer += "A"
    elif idx == 1:
        answer += "C"
    elif idx == 2:
        answer += "G"
    elif idx == 3:
        answer += "T"
    HD += (N-max(RNA))
print(answer)
print(HD)
