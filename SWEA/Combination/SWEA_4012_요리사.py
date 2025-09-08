# SWEA 4012. [모의 SW 역량테스트] 요리사
import sys
sys.stdin = open("input.txt", "r")


def cook(team):
    total = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            a, b = team[i], team[j]
            total += matrix[a][b] + matrix[b][a]
    return total


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    case = []
    for idx in range(1 << N):
        mask = idx
        arr = []
        for n in range(N):
            if mask & 0x1:
                arr.append(n)
            mask >>= 1
        if len(arr) == N // 2:
            case.append(arr)
    results = []

    for idx in range(len(case) // 2):
        results.append(abs(cook(case[idx]) - cook(case[-1 - idx])))

    print(f'#{tc} {min(results)}')
