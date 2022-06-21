#BJ1013. Contact

def pattern(text):
    if len(text) <= 3:
        print("YES")
        return "YES"
    elif len(text) == 4:
        print("NO")
        return "NO"
    else:
        if text[0] == '0':
            if text[1] == '1':
                pattern(text[2:])
            else:
                print("NO")
                return "NO"
        else:
            if 5 <= len(text) <= 6:
                print("NO")
                return "NO"
            elif text[1] == "0" and text[2] == "0":
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
                pattern(text[idx-1:])

            else:
                print("NO")
                return "NO"



T = int(input())

for _ in range(T):
    sign = input()
    sign += "000"
    pattern(sign)