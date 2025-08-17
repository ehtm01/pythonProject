# 1974. 스도쿠 검증
def sdoku():
    sdoku_set = set(range(1, 10))

    for row in matrix:
        if set(row) != sdoku_set:
            return 0

    for col in zip(*matrix):
        if set(col) != sdoku_set:
            return 0

    for r in range(N // 3):
        for c in range(N // 3):
            matrix_m = []
            for i in range(N // 3):
                for j in range(N // 3):
                    a = i + 3 * r
                    b = j + 3 * c
                    matrix_m.append(matrix[a][b])
            if set(matrix_m) != sdoku_set:
                return 0

    return 1


T = int(input())

for tc in range(1, T + 1):
    N = 9
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {sdoku()}')
