from itertools import combinations

def play(n):
    global ans
    if n == 15:
        ans = 1
        for r in results:
            if r.count(0) != 3:
                ans = 0
                break
        return
    
    x, y = combi[n]
    
    for r1, r2 in ((2,0),(1,1),(0,2)):
        if results[x][r1] > 0 and results[y][r2] > 0:
            results[x][r1] -= 1
            results[y][r2] -= 1
            play(n+1)
            results[x][r1] += 1
            results[y][r2] += 1

combi = list(combinations(range(6),2))
answer = []
for i in range(4):
    arr = list(map(int, input().split()))
    results = []
    for j in range(6):
        results.append(arr[3*j:3*j+3])
    ans = 0
    play(0)
    answer.append(ans)
    
print(*answer)