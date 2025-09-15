# SWEA 17015. 6일차 응용 - 그룹 나누기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def find_set(x):
    while parents[x] != x:
        parents[x], x = parents[parents[x]], parents[x]
    return x


def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return

    if ranks[rep_x] < ranks[rep_y]:
        rep_x, rep_y = rep_y, rep_x
    parents[rep_y] = rep_x
    if ranks[rep_x] == ranks[rep_y]:
        ranks[rep_x] += 1


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = list(range(N + 1))
    ranks = [0] * (N + 1)

    for i in range(M):
        a = arr[2 * i]
        b = arr[2 * i + 1]
        union(a, b)

    result = len({find_set(i) for i in range(1, N + 1)})
    print(ranks)
    print(f'#{tc} {result}')
