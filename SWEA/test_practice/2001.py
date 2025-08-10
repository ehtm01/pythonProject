# 2001. 파리 퇴치

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            curr_kill = 0
            for a in range(M):
                for b in range(M):
                    curr_kill += matrix[i+a][j+b]
            max_kill = max(max_kill, curr_kill)

    print(f'#{tc} {max_kill}')
