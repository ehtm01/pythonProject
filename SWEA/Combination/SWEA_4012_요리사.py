# SWEA 4012. [모의 SW 역량테스트] 요리사
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    foods = list(range(N))
    case = []

    for i in range(1 << N):
        arr = []
        for n in range(N):
            if i & 0x1:
                arr.append(foods[n])
            i >>= 1
        if len(arr) == N / 2:
            case.append(arr)
    results = []

    subset = []
    A = B = 0

    def cook(idx, start):
        global A, B
        if idx == N // 2:
            x, y = subset[0], subset[1]
            a, b = N - subset[0] - 1, N - subset[1] - 1
            A += (matrix[x][y] + matrix[y][x])
            B += (matrix[a][b] + matrix[b][a])
            return

        for i in range(len(case) // 2):
            for j in range(start, N // 2):
                subset.append(case[i][j])
                cook(idx + 1, j + 1)
                subset.pop(0)
            results.append(abs(A - B))

    cook(0, 0)

    # print(case)
    print(min(results))
