import sys
sys.stdin = open('input.txt', 'r')

from copy import deepcopy


# 배열 회전시켜야 함
# temp값 하나 잡고 나머지 4면으로 돌리자
# 마지막에 temp값 넣어주면 끝
def spin(row, col, step, matrix):
    temp = matrix[row][col + step]
    for j in range(step, 0, -1):
        matrix[row][col + j] = matrix[row][col + j - 1]
    for i in range(step):
        matrix[row + i][col] = matrix[row + i + 1][col]
    for j in range(step):
        matrix[row + step][col + j] = matrix[row + step][col + j + 1]
    for i in range(step, 1, -1):
        matrix[row + i][col + step] = matrix[row + i - 1][col + step]
    matrix[row + 1][col + step] = temp
    if step >= 3:
        spin(row + 1, col + 1, step - 2, matrix)
    return matrix


# K 크기의 배열에 저장된 (r, c, s)
# 순열을 통해서 여러 가지 케이스로 최솟값 내야함
# spin 함수의 반환값으로 비교해보자
def compare(cnt, arr):
    global best

    if cnt == K:
        matrix = deepcopy(grid)
        for row, col, step in arr:
            spin(row - step - 1, col - step - 1, step * 2, matrix)
        best = min(best, min([sum(j) for j in matrix]))

    for i in range(K):
        if used[i]:
            continue
        used[i] = True
        arr.append(a[i])
        compare(cnt + 1, arr)
        arr.pop()
        used[i] = False


N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

a = []
for _ in range(K):
    r, c, s = map(int, input().split())
    a.append((r, c, s))

used = [False] * K
best = float('inf')
compare(0, [])

print(best)
