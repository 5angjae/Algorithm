# BOJ16637 괄호 추가하기
import copy
from collections import deque

def part_num(signs, temp):
    a = copy.deepcopy(temp) # 얕은 복사를 하게 되면 서로 같은 주소를 바라보기 때문에 temp값이 바뀌게 된다. 따라서 깊은 복사 사용
    signs_combi.append(a)

    if len(signs) - temp[-1] > 2:
        for i in range(len(signs)-temp[-1] - 2):
            temp.append(temp[-1] + 2 + i)
            part_num(signs, temp)
            temp.pop()

def cal(x, y, sign):
    if sign == "+":
        return x + y
    elif sign == "-":
        return x - y
    elif sign == "*":
        return x * y


N = int(input())
poly = input()
numbers = []
signs = []
for i in range(len(poly)):
    if i%2 == 0:
        numbers.append(int(poly[i]))
    else:
        signs.append(poly[i])

# max_combi_size = len(signs) // 2 + len(signs) % 2
signs_combi = [[]]

for i in range(len(signs)):
    temp = [i]
    part_num(signs, temp)

max_num = -(2**31)
for combi in signs_combi:
    # combi 내의 인덱스 각각에 대해서 (idx)
    # numbers[idx] signs[idx] numbers[idx+1] 을 계산한 값을 numbers list에 다시 넣고 (어떻게 넣을지 생각)
    new_num = deque()
    new_sign = []
    for i in range(len(signs)):
        if i in combi:
            new_num.append(cal(numbers[i], numbers[i+1], signs[i]))
        else:
            new_sign.append(signs[i])
            if (i-1) not in combi:
                new_num.append(numbers[i])

    if len(combi) > 0:
        if combi[-1] != len(signs):
            new_num.append(numbers[len(signs)])
    else:
        new_num.append(numbers[len(signs)])

    for i in range(len(new_sign)):
        a = new_num.popleft()
        b = new_num.popleft()
        c = cal(a, b, new_sign[i])
        new_num.appendleft(c)

    if new_num[0] > max_num:
        max_num = new_num[0]

print(max_num)



# 괄호 조합을 다 찾는다.
# 계산을 한다.
# 최대값이 아니면 넘어간다.

# 연산자 우선순위는 무조건 동일
# 괄호만 우선
# 괄호 안에는 하나의 연산자만 - 그 해당 연산만 먼저 처리하고 대체 해놓고, 전체 연산하면 되긴 함
# 연산자 개수를 센다.
# 연산자를 선택할 수 있는 모든 조합을 고려하는데 바로 연결된 연산자를 고를 순 없다.
# 연산자 인덱스를 기준으로 조합을 만든다. (0 ~ 4 까지 인덱스가 있는 경우)
# (0), (1), (2), (3), (4), (0, 2), (0,3), (0,4), (1,3), (1,4), (2, 4), (0, 2, 4)
# 이런 식으로 우선 연산을 할 수 있는 조합을 정리한다.
# 각 조합별로,
#
# 3, 8, 7, 9, 2
# + * - *
# (0)
# 3 8  (7, 9, 2)
# + (* - *)
# 11 7 9 2
# * - *