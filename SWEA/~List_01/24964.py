# 24964. 2차원배열의합02
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    num_sum = 0

    for i in range(N):
        for j in range(M):
            num_sum += matrix[i][j]

    print(f'#{tc} {num_sum}')
