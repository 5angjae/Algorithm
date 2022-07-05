N = int(input())
numbers = list(map(int, input().split()))
P = [[0] * N for _ in range(N)]
P[N-1][N-1] = 1
for i in range(N-1):
    P[i][i] = 1
    if numbers[i] == numbers[i+1]:
        P[i][i+1] = 1
    L,R=i,i
    l,r=i,i+1
    while P[L][R]==1 or P[l][r]==1:
        nL,nR = L-1, R+1
        nl,nr = l-1, r+1
        #print(nL,nR,nl,nr)
        if nL < 0 or nl < 0:
            break
        if numbers[nL]==numbers[nR]:
            P[nL][nR] = 1
        if nR >= N or nr >= N:
            break
        if numbers[nl]==numbers[nr]:
            P[nl][nr] = 1
        L = nL
        R = nR
        l = nl
        r = nr

#print(P)
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(P[S-1][E-1])