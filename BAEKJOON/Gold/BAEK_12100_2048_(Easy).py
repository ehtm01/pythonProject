# BAEK 12100. 2048 (Easy)
import sys
sys.stdin = open('input.txt', 'r')
from copy import deepcopy

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


def moving(dirs, grid):
    if not dirs % 2:
        if dirs // 2:
            for i in range(1, N):
                for j in range(N):
                    if grid[i][j]:
                        if grid[i - 1][j]:
                            if grid[i - 1][j] == grid[i][j]:
                                grid[i - 1][j] += grid[i][j]
                                grid[i][j] = 0
                        else:
                            a = i
                            while a > 0:
                                if grid[a - 1][j]:
                                    if grid[a - 1][j] == grid[a][j]:
                                        grid[a - 1][j] += grid[a][j]
                                        grid[a][j] = 0
                                else:
                                    grid[a - 1][j] = grid[a][j]
                                    grid[a][j] = 0
                                a -= 1
        else:
            for i in range(N - 2, -1, -1):
                for j in range(N):
                    if grid[i][j]:
                        if grid[i + 1][j]:
                            if grid[i + 1][j] == grid[i][j]:
                                grid[i + 1][j] += grid[i][j]
                                grid[i][j] = 0
                        else:
                            a = i
                            while a < N - 1:
                                if grid[a + 1][j]:
                                    if grid[a + 1][j] == grid[a][j]:
                                        grid[a + 1][j] += grid[a][j]
                                        grid[a][j] = 0
                                else:
                                    grid[a + 1][j] = grid[a][j]
                                    grid[a][j] = 0
                                a += 1
    else:
        if dirs // 2:
            for j in range(1, N):
                for i in range(N):
                    if grid[i][j]:
                        if grid[i][j - 1]:
                            if grid[i][j - 1] == grid[i][j]:
                                grid[i][j - 1] += grid[i][j]
                                grid[i][j] = 0
                        else:
                            a = j
                            while a > 0:
                                if grid[i][a - 1]:
                                    if grid[i][a - 1] == grid[i][a]:
                                        grid[i][a - 1] += grid[i][a]
                                        grid[i][a] = 0
                                else:
                                    grid[i][a - 1] = grid[i][a]
                                    grid[i][a] = 0
                                a -= 1
        else:
            for j in range(N - 2, -1, -1):
                for i in range(N):
                    if grid[i][j]:
                        if grid[i][j + 1]:
                            if grid[i][j + 1] == grid[i][j]:
                                grid[i][j + 1] += grid[i][j]
                                grid[i][j] = 0
                        else:
                            a = j
                            while a < N - 1:
                                if grid[i][a + 1]:
                                    if grid[i][a + 1] == grid[i][a]:
                                        grid[i][a + 1] += grid[i][a]
                                        grid[i][a] = 0
                                else:
                                    grid[i][a + 1] = grid[i][a]
                                    grid[i][a] = 0
                                a += 1
    ans = 0
    for arr in grid:
        ans = max(ans, max(arr))
    return ans


def backtrack(cnt, g, res):
    global max_block

    if cnt == 5:
        max_block = max(max_block, res)
        return

    for i in range(4):
        mat = deepcopy(g)
        ans = moving(i, mat)
        backtrack(cnt + 1, mat, ans)


max_block = 0
backtrack(0, matrix, 0)
print(max_block)
