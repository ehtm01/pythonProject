# 1227. [S/W 문제해결 기본] 7일차 - 미로2
from collections import deque

T = 10

for tc in range(1, T + 1):
    t = input()
    N = 100
    maze = [input() for _ in range(N)]
    s = (1, 1)
    q = deque()
    q.append(s)
    visited = [[0] * N for _ in range(N)]
    visited[2][2] = 1
    d = (-1, 0), (1, 0), (0, -1), (0, 1)

    # print(maze)
    def BFS():
        while q:
            i, j = q.popleft()
            if maze[i][j] == '3':
                return 1
            for di, dj in d:
                ni, nj = i + di, j + dj
                if (0 <= ni < N and 0 <= nj < N and
                        not visited[ni][nj] and
                        maze[ni][nj] != '1'):
                    q.append((ni, nj))
                    visited[ni][nj] = 1

        return 0

    print(f'#{tc} {BFS()}')
