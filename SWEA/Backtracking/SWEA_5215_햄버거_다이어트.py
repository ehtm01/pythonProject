# SWEA 5215. 햄버거 다이어트
import sys
sys.stdin = open("input.txt", "r")


def backtrack(idx, sum_s, sum_c):
    global max_score
    if sum_c > L:
        return
    if idx == N:
        max_score = max(max_score, sum_s)
        return

    backtrack(idx + 1, sum_s + combo[idx][0], sum_c + combo[idx][1])
    backtrack(idx + 1, sum_s, sum_c)


T = int(input())

for tc in range(1, T +1):
    N, L = map(int, input().split())
    combo = []
    for _ in range(N):
        s, c = map(int, input().split())
        combo.append((s, c))

    max_score = 0

    backtrack(0, 0, 0)
    print(f'#{tc} {max_score}')
