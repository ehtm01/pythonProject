# SWEA 25052. 등산로
from collections import deque

def find_way(row, col):
    global max_len
    q = deque([(row, col)])
    x, y = row, col

    while q:
        r, c = q.popleft()
        min_h = height[r][c]
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if (0 <= nr < N and 0 <= nc < N and
                height[nr][nc] < min_h):
                min_h = height[nr][nc]
                x = nr
                y = nc

        if (r, c) != (x, y):
            q.append((x, y))
            visited[x][y] = visited[r][c] + 1
            max_len = max(max_len, visited[x][y])


T = int(input())
d = (-1, 0), (1, 0), (0, -1), (0, 1)

for tc in range(1, T + 1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]
    max_len = 1

    for i in range(N):
        for j in range(N):
            find_way(i, j)

    print(f'#{tc} {max_len}')
