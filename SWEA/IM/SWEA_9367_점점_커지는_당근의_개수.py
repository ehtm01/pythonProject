# 9367. 점점 커지는 당근의 개수
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    l = 1
    max_l = 0

    for i in range(1, N):
        if C[i - 1] < C[i]:
            l += 1
        else:
            l = 1
        if max_l < l:
            max_l = l

    print(f'#{tc} {max_l}')
