# 16532. 5일차 - 미로
def find_path(matrix, s1, s2):
    i, j = s1, s2
    N = len(matrix)
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = [[0] * N for _ in range(N)]
    stack = []
    visited[i][j] = 1

    while True:
        if matrix[i][j] == 3:
            return 1

        for di, dj in d:
            ni, nj = i + di, j + dj
            if ((0 <= ni < N and 0 <= nj < N) and
                (matrix[ni][nj] != 1) and
                (not visited[ni][nj])):
                visited[ni][nj] = 1
                stack.append((i, j))
                i, j = ni, nj
                break
        else:
            if stack:
                i, j = stack.pop()
            else:
                break
    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 2:
                s1, s2 = r, c

    print(f'#{tc} {find_path(matrix, s1, s2)}')
