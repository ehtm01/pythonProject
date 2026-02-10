# 1868. 파핑파핑 지뢰찾기
from collections import deque


def find_mine():
    for r in range(N):
        for c in range(N):
            if mine[r][c] == '*':
                visited[r][c] = 1
                mine_sum[r][c] = -1
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and mine_sum[nr][nc] != -1:
                        mine_sum[nr][nc] += 1


def minesweeper(row, col):
    q.append((row, col))
    visited[row][col] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and mine[nx][ny] != '*':
                visited[nx][ny] = 1
                if mine_sum[nx][ny] == 0:
                    q.append((nx, ny))


T = int(input())
d = (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)

for tc in range(1, T + 1):
    N = int(input())
    mine = [list(map(str, input())) for _ in range(N)]
    click_cnt = 0
    mine_sum = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q = deque()

    find_mine()

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and mine_sum[i][j] == 0:
                click_cnt += 1
                minesweeper(i, j)

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and mine_sum[i][j] > 0:
                click_cnt += 1

    print(f'#{tc} {click_cnt}')
