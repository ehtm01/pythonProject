import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


def spin(row, col, space, cnt, t):

    if cnt == 4:
        if space > 3:
            spin(row + 1, col + 1, space - 2, 0, 0)
        else:
            return

    temp = matrix[row][col + space]
    for j in range(col + space, col, -1):
        matrix[row][j] = matrix[row][j - 1]
    if t:
        matrix[row][col] = t

    spin(col, row, space, cnt + 1, temp)








for _ in range(K):
    r, c, s = map(int, input().split())
    spin(r - s - 1, c - s - 1, s * 2, 0)
