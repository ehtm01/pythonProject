# BAEK 12100. 2048 (Easy)
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
d = (1, 0), (0, 1), (-1, 0), (0, -1)


def is_moved(d):
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                visited[i][j] = 1
    pass


def backtrack(cnt, d):
    global best
    direction = d
    if cnt == 5:
        for arr in grid:
            num = max(arr)
            best = max(best, num)
        return
    if not is_moved(direction):
        return



best = 0
backtrack(0, 0)
