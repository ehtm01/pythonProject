def solution(new_id):
    string = ''

    for ch in new_id.lower():
        if ch in 'abcdefghijklmnopqrstuvwxyz0123456789-_':
            string += ch
        elif ch == '.' and not string.endswith('.'):
            string += ch

    # 처음과 끝의 마침표 제거
    new_id = string.strip('.')

    if not new_id:
        new_id = 'a'

    # 길이를 줄인 뒤 끝에 생긴 마침표 제거
    new_id = new_id[:15].rstrip('.')

    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id