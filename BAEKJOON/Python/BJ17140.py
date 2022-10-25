def sort_arr(A):
    temp = []
    max_len = 0
    for a in A:
        temp_dict = {}
        for ele in a:
            if ele != 0:
                if ele not in temp_dict:
                    temp_dict[ele] = 1
                else:
                    temp_dict[ele] += 1
        temp_list = sorted(temp_dict.items(), key=lambda x: (x[1], x[0]))
        #print(temp_list)
        temp_append = []
        len_arr = 0
        for t in temp_list:
            temp_append.append(t[0])
            temp_append.append(t[1])
            len_arr += 2
        if max_len < len_arr:
            max_len = len_arr
        temp.append(temp_append)
        #print(temp, "!!@#!@#")
    # 길이 맞추기
    temp1 = []
    for t in temp:
        temp_new = []
        if len(t) < max_len:
            for tn in t:
                temp_new.append(tn)
            for _ in range(max_len - len(t)):
                temp_new.append(0)
        else:
            temp_new = t
        temp1.append(temp_new)
    return temp1

def change_arr(A):
    temp = []
    for i in range(len(A[0])):
        temp_arr = []
        for j in range(len(A)):
            temp_arr.append(A[j][i])
        temp.append(temp_arr)
    return temp

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

answer = 0
cnt = 0
# A[r][c] == k 가 될때까지 반복 - index에러로 while문 조건에는 적을 수 없고, if 문에 break로
while cnt <= 100:
    if len(A) > r-1 and len(A[0]) > c-1:
        if A[r-1][c-1] == k:
            answer = cnt
            break

    if len(A) >= len(A[0]): # R연산
        A = sort_arr(A)
        #print(A)
    else: # C연산
        A = change_arr(A)
        A = sort_arr(A)
        A = change_arr(A)
    cnt += 1
    #print(A)

if cnt > 100:
    print(-1)
else:
    print(cnt)