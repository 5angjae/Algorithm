import itertools

def check(arr, co):
    students = []
    teachers = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "S":
                students.append([i, j])
            elif arr[i][j] == "T":
                teachers.append([i, j])
    # print(students)
    # print(teachers)
    cnt = 0
    cnt1 = 0
    for s in students:
        for t in teachers:
            state = 0
            # print("!", s, t, co)
            if s[0] == t[0]:
                cnt1 += 1
                for c in co:
                    if c[0] == s[0]:

                        if s[1] < c[1] < t[1] or t[1] < c[1] < s[1]:
                            state = 1
                            break
            elif s[1] == t[1]:
                cnt1 += 1
                for c in co:
                    if c[1] == s[1]:

                        if s[0] < c[0] < t[0] or t[0] < c[0] < s[0]:
                            state = 1
                            break
            if state == 1:
                # print(s, t, "check")
                cnt += 1
    if cnt == cnt1:
        #print(cnt, cnt1)
        return True
    else:
        #print(cnt, cnt1)
        return False

N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
# 36칸에서 3개 조합
# 36*35*34 = 42000쯤 - 전부 해도 상관 X
positions = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == "X":
            positions.append([i, j])

comb = list(itertools.combinations(positions, 3))

# print(list(comb))

state1 = 0
for co in comb:
    # print("===============")
    if check(arr, co):
        print("YES")
        state1 = 1
        break

if state1 == 0:
    print("NO")

