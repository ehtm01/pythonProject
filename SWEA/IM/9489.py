# 9489. 고대 유적
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_len = 0

    for r in range(N):
        structure_len = 0
        for c in range(M):
            if data[r][c] == 1:
                structure_len += 1
                max_len = max(max_len, structure_len)
            else:
                structure_len = 0

    for c in range(M):
        structure_len = 0
        for r in range(N):
            if data[r][c] == 1:
                structure_len += 1
                max_len = max(max_len, structure_len)
            else:
                structure_len = 0

    print(f'#{tc} {max_len}')
