# 2001. 파리 퇴치
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_fly = 0
            for r in range(i, i + M):
                for c in range(j, j + M):
                    sum_fly += matrix[r][c]
            max_sum = max(max_sum, sum_fly)

    print(f'#{tc} {max_sum}')