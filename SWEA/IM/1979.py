# 1979. 어디에 단어가 들어갈 수 있을까
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        r = c = 0
        for j in range(N):
            if matrix[i][j]:
                r += 1
            else:
                if r == K:
                    result += 1
                r = 0
            if matrix[j][i]:
                c += 1
            else:
                if c == K:
                    result += 1
                c = 0
        if r == K:
            result += 1
        if c == K:
            result += 1

    print(f'#{tc} {result}')
