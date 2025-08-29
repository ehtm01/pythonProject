# SWEA 5432. 쇠막대기 자르기
T = int(input())

for tc in range(1, T + 1):
    arr = list(map(str, input()))
    bar = result = 0
    prev = ''

    for i in arr:
        if i == '(':
            bar += 1
        else:
            bar -= 1
            if prev == '(':
                result += bar
            else:
                result += 1
        prev = i

    print(f'#{tc} {result}')
