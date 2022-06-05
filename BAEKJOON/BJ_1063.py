def position(move, now_text):
    now = [now_text[0], int(now_text[1])]
    next_position = [0, 0]
    if move == "R":
        next_position[0] = ord(now[0]) + 1
        next_position[1] = now[1]
    elif move == "L":
        next_position[0] = ord(now[0]) - 1
        next_position[1] = now[1]
    elif move == "B":
        next_position[0] = ord(now[0])
        next_position[1] = now[1] - 1
    elif move == "T":
        next_position[0] = ord(now[0])
        next_position[1] = now[1] + 1
    elif move == "RT":
        next_position[0] = ord(now[0]) + 1
        next_position[1] = now[1] + 1
    elif move == "LT":
        next_position[0] = ord(now[0]) - 1
        next_position[1] = now[1] + 1
    elif move == "RB":
        next_position[0] = ord(now[0]) + 1
        next_position[1] = now[1] - 1
    elif move == "LB":
        next_position[0] = ord(now[0]) - 1
        next_position[1] = now[1] - 1

    if 65 <= next_position[0] < 73 and 1 <= next_position[1] < 9:
        result = chr(next_position[0]) + str(next_position[1])
        return result
    else:
        return 0

King, Stone, n = map(str, input().split())
N = int(n)
for _ in range(N):
    move = input()
    if position(move, King) == 0:
        continue
    elif position(move, King) == Stone:

        if position(move, Stone) == 0:
            continue
        else:
            King = position(move, King)
            Stone = position(move, Stone)
    else:
        King = position(move, King)

print(King)
print(Stone)