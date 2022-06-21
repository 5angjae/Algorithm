# 1013 Contact 다시 풀기
# 어디서 indexError가 뜨는건지 확인할 필요가 있다.

import sys
input = sys.stdin.readline
def pattern(text):
    if len(text) == 0:
        print("YES")
        return
    else:
        if text[0] == "0":
            if text[1] == "1":
                pattern(text[2:])
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
                        idx += 1
                    if change == 2:
                        pattern(text[idx - 1:])
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
texts = [input().strip() for _ in range(T)]
for text in texts:
    if len(text) == 0:
        print("NO")
    else:
        pattern(text)