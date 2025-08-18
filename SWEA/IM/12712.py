# 12712. 파리퇴치3
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    d_plus = (-1, 0), (1, 0), (0, -1), (0, 1)
    d_x = (-1, -1), (1, -1), (1, 1), (-1, 1)
    max_sum = 0

    for r in range(N):
        for c in range(N):
            sum_kill_plus = sum_kill_x = matrix[r][c]
            for k in range(1, M):
                for di, dj in d_plus:
                    ni, nj = r + k * di, c + k * dj
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_kill_plus += matrix[ni][nj]
                for di, dj in d_x:
                    ni, nj = r + k * di, c + k * dj
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_kill_x += matrix[ni][nj]
            max_sum = max(max_sum, sum_kill_plus, sum_kill_x)

    print(f'#{tc} {max_sum}')
