# BOJ 13904 과제
# 시간 초과

N = int(input())

homeworks = []
for i in range(N):
    d, w = map(int, input().split())
    homeworks.append([d, w, i])

homeworks.sort(reverse=True)
max_day = homeworks[0][0]
end_homework = []
point = 0
for i in range(max_day, 0, -1):
    max_daily_point = 0
    max_homework = []
    for homework in homeworks:
        if homework[0] >= i and homework[1] > max_daily_point and homework not in end_homework:
            max_daily_point = homework[1]
            max_homework = homework
            # print("for", i, homework, max_daily_point)


    end_homework.append(max_homework)
    # print("out", i, end_homework, max_daily_point)
    point += max_daily_point

print(point)

#   1   2   3   4   5   6
#                       5
#                   0
#               60
#           40
#       50
#   30