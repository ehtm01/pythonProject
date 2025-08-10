# 12712. 파리퇴치3

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    plus = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    max_kill = 0

    for i in range(N):
        for j in range(N):
            plus_kill = x_kill = matrix[i][j]
            for di, dj in plus:
                for power in range(1, M):
                    ni, nj = i + di * power, j + dj * power
                    if 0 <= ni < N and 0 <= nj < N:
                        plus_kill += matrix[ni][nj]
            for di, dj in x:
                for power in range(1, M):
                    ni, nj = i + di * power, j + dj * power
                    if 0 <= ni < N and 0 <= nj < N:
                        x_kill += matrix[ni][nj]
            max_kill = max(max_kill, plus_kill, x_kill)

    print(f'#{tc} {max_kill}')
