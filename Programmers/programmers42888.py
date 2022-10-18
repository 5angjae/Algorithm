def solution(record):
    answer = []
    temp = []
    uid_nick = {}
    for r in record:
        a = list(map(str, r.split()))
        temp.append([a[1], a[0]])
        if a[0] != "Leave":
            uid_nick[a[1]] = a[2]

    for t in temp:
        if t[1] == "Enter":
            answer.append(f"{uid_nick[t[0]]}님이 들어왔습니다.")
        elif t[1] == "Leave":
            answer.append(f"{uid_nick[t[0]]}님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))