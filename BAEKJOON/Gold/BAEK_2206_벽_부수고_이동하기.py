# BAEK 2206. 벽 부수고 이동하기
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
grid = [str(input()) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
q = deque([(0, 0, 1)])
visited[0][0][1] = 1

while q:
    y, x, cnt = q.popleft()

    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if not (0 <= ny < N and 0 <= nx < M):
            continue

        if grid[ny][nx] == '0' and visited[ny][nx][cnt] == -1:
            visited[ny][nx][cnt] = visited[y][x][cnt] + 1
            q.append((ny, nx, cnt))

        elif grid[ny][nx] == '1' and cnt == 1 and visited[ny][nx][0] == -1:
            visited[ny][nx][0] = visited[y][x][cnt] + 1
            q.append((ny, nx, 0))

res = -1
v0 = visited[N-1][M-1][0]
v1 = visited[N-1][M-1][1]
if v0 != -1 and v1 != -1:
    res = v0 if v0 < v1 else v1
elif v0 != -1:
    res = v0
elif v1 != -1:
    res = v1

print(res)
