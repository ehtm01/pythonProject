# BAEK 15683. 감시
import sys
sys.stdin = open('input.txt', 'r')
from copy import deepcopy

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
u = (-1, 0)
r = (0, 1)
d = (1, 0)
l = (0, -1)

d = {
    1: [[u], [r], [d], [l]],
    2: [[u, d], [l, r]],
    3: [[u, r], [r, d], [d, l], [l, u]],
    4: [[l, u, r], [u, r, d], [r, d, l], [d, l, u]],
    5: [[u, r, d, l]]
}


def watch(g, r, c, direction):
    for dr, dc in direction:
        nr, nc = r + dr, c + dc
        while 0 <= nr < N and 0 <= nc < M:
            if g[nr][nc] == 6:
                break
            if g[nr][nc] == 0:
                g[nr][nc] = '#'
            nr += dr
            nc += dc


def dfs(idx, board):
    global result
    if idx == len(cctv):
        # 남은 사각지대 개수 세기
        cnt = 0
        for row in board:
            cnt += row.count(0)
        result = min(result, cnt)
        return


cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= matrix[i][j] <= 5:
            cctv.append((matrix[i][j], i, j))

result = N * M
