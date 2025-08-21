# 16674. 6일차 - 미로의 거리
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    q = deque()
    move = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    def find_move():
        for i in range(N):
            for j in range(N):
                if maze[i][j] == '2':
                    q.append((i, j))
                    break
            if q:
                break
        while q:
            r, c = q.popleft()
            if not visited[r][c]:
                visited[r][c] = True
                for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        if maze[nr][nc] == '0':
                            q.append((nr, nc))
                            move[nr][nc] = move[r][c] + 1
                        elif maze[nr][nc] == '3':
                            return move[r][c]
        return 0

    print(f'#{tc} {find_move()}')
