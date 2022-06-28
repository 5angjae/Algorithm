# 1013 Contact 다시 풀기
# 어디서 indexError가 뜨는건지 확인할 필요가 있다.

import sys
# (100+1+|01)+
# 10011001
def pattern(text):
    # print(text)
    if len(text) == 0:
        print("YES")
        return
    elif len(text) == 1: # text 길이가 1이 되면 01, 100 을 찾기 위해서 탐색할 때 인덱스 에러가 난다.
        print("NO")
        return
    else:
        if text[0] == "0":
            if text[1] == "1":
                pattern(text[2:])
                return
            else:
                print("NO")
                return
        else:
            if len(text) < 4:
                print("NO")
                return
            else:

                if text[1] == "0" and text[2] == "0":
                    change = 0
                    idx = 3
                    state = 0

                    while change < 2 and idx < len(text):
                        if text[idx] == "0" and state == 1:
                            change += 1
                            state = 0
                        elif text[idx] == "1" and state == 0:
                            change += 1
                            state = 1
                        if change == 1 and text[idx+1:idx+4] == "100": # 1001/1001 연달아 나올 때 잘못 나눠줘서 해결하기 위한 코드
                            break
                        idx += 1
                    if change == 1 and text[idx+1:idx+4] =="100":
                        pattern(text[idx+1:])
                        return
                    if change == 2:
                        pattern(text[idx - 1:])
                        return
                    if idx == len(text):
                        if change == 1:
                            print("YES")
                            return
                        else:
                            print("NO")
                            return
                else:
                    print("NO")
                    return


T = int(input())
texts = [input() for _ in range(T)]
for text in texts:
    if len(text) == 0:
        print("NO")
    else:
        pattern(text)