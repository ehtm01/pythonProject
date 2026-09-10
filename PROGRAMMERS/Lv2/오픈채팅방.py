def solution(record):
    answer = []
    user_dict = {}
    for s in record:
        lst = s.split()
        if lst[0] == 'Enter':
            user_dict[lst[1]] = lst[2]
            answer.append(lst[1] + " 님이 들어왔습니다.")
        elif lst[0] == 'Leave':
            answer.append(lst[1] + " 님이 나갔습니다.")
        else:
            user_dict[lst[1]] = lst[2]

    result = []
    for a in answer:
        lst = a.split()
        result.append(user_dict[lst[0]] + lst[1] + " " + lst[2])
    return result
