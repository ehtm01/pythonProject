# 11092. 최대 최소의 간격
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    number = list(map(int, input().split()))
    max_num = min_num = number[0]
    max_idx = min_idx = 0

    if 1 in number:
        min_idx = number.index(1)

    for i in range(len(number)):
        if max_num <= number[i]:
            max_num = number[i]
            max_idx = i
        if min_num > number[i]:
            min_num = number[i]
            min_idx = i

    result = 0
    if max_idx >= min_idx:
        result = max_idx - min_idx
    else:
        result = min_idx - max_idx

    print(f'#{tc} {result}')
