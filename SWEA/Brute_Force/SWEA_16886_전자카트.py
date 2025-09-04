# SWEA 16886. 2일차 응용 - 전자카트
import sys
sys.stdin = open("input.txt", "r")


def solve(c, n):
    global min_sum

    if min_sum and min_sum < sum(path):
        return

    if n == N:
        if min_sum:
            min_sum = min(min_sum, sum(path))
        else:
            min_sum = sum(path)

    if len(path) != N - 1:
        for i in range(1, N):
            if visited[i] == 0 and c != i:
                visited[i] = 1
                path.append(matrix[c][i])
                solve(i, n + 1)
                path.pop()
                visited[i] = 0
    else:
        visited[0] = 1
        path.append(matrix[c][0])
        solve(0, n + 1)
        path.pop()
        visited[0] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    path = []
    min_sum = current = 0
    visited = [0] * N

    solve(0, 0)

    print(f'#{tc} {min_sum}')
