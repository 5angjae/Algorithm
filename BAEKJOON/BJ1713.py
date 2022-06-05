# BJ1713 후보 추천하기
# 너무 오랜만에 해서 문제가 안읽혀요
# 후보틀 / 가득찼을 때 새로운 후보 추천 - 가장 적은 학생 사진 삭제 후, 그 자리

N = int(input())
R = int(input())
R_list = list(map(int, input().split()))

photo = dict()
for i in range(R):
    if R_list[i] in photo:
        photo[R_list[i]][0] += 1
    else:
        if len(photo) < N:
            photo[R_list[i]] = [1, i]
        else: # 사진틀이 가득차있을 경우
            del_list = sorted(photo.items(), key = lambda x : (x[1][0], x[1][1]))
            del_key = del_list[0][0]
            del(photo[del_key])
            photo[R_list[i]] = [1, i]

ans_list = list(sorted(photo.keys()))
print(' '.join(map(str, ans_list)))