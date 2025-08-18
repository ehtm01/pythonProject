# 9490. 풍선팡
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flower = [list(map(int, input().split())) for _ in range(N)]
    d = (-1, 0), (1, 0), (0, -1), (0, 1)
    max_sum = 0

    for r in range(N):
        for c in range(M):
            flower_sum = flower[r][c]
            for dr, dc in d:
                for k in range(1, flower[r][c] + 1):
                    nr, nc = r + k * dr, c + k * dc
                    if 0 <= nr < N and 0 <= nc < M:
                        flower_sum += flower[nr][nc]
                    else:
                        break
            max_sum = max(max_sum, flower_sum)

    print(f'#{tc} {max_sum}')
