# 10760. 우주선착륙2
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    d = (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)
    ok = 0

    for i in range(N):
        for j in range(M):
            center = data[i][j]
            cnt = 0
            for di, dj in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and data[ni][nj] < center:
                    cnt += 1
                    if cnt >= 4:
                        ok += 1
                        break

    print(f'#{tc} {ok}')
