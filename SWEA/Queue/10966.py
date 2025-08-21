# 10966. 물놀이를 가자
from collections import deque

def bfs():
    visited = [[-1] * M for _ in range(N)]

    while wq:
        x, y = wq.popleft()
        visited[x][y] += 1
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and str_map[nx][ny] != 'W':
                wq.append((nx, ny))
                visited[nx][ny] = visited[x][y]

    return visited

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    str_map = [input() for _ in range(N)]
    result = 0
    wq = deque()

    for i in range(N):
        for j in range(M):
            if str_map[i][j] == 'W':
                wq.append((i, j))

    # print(bfs())
    print(f'#{tc} {sum(map(sum, bfs()))}')
