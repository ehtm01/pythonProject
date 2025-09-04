# SWEA 16883. 최소합
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
d = (0, 1), (1, 0)

def solve(si, sj):
    global min_sum

    if (si, sj) == (N - 1, N - 1):
        if min_sum:
            min_sum = min(min_sum, sum(path))
        else:
            min_sum = sum(path)
        return

    for di, dj in d:
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            path.append(matrix[ni][nj])
            solve(ni, nj)
            path.pop()
            visited[ni][nj] = 0


for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    path = [matrix[0][0]]
    min_sum = 0
    solve(0, 0)

    print(f'#{tc} {min_sum}')
