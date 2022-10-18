import math


def solution(w, h):
    answer = w * h

    if w == h:
        answer = w * h - w

    else:
        gcd = math.gcd(w, h)
        a = min(w // gcd, h // gcd)
        b = max(w // gcd, h // gcd)

        if a == 1 or b == 1:
            cnt = max(a,b)
        else:
            temp = []
            for i in range(1, a + 1):
                temp.append(b * i // a + 1)
            # print(temp)
            cnt = temp[0]
            for i in range(1, len(temp) - 1):
                cnt += temp[i] - temp[i - 1] + 1
            cnt += temp[0]

        answer = answer - cnt * gcd

    return answer

print(solution(9,3))
