# SWEA 1244. [S/W 문제해결 응용] 2일차 - 최대 상금
import sys
sys.stdin = open("input.txt", "r")


def solve(c):
    global max_bonus

    if (c, ''.join(map(str, nums))) in check:
        return
    check.add((c, ''.join(map(str, nums))))

    if c == C:
        max_bonus = max(max_bonus, int(''.join(map(str, nums))))
        return

    for i in range(M - 1):
        for j in range(i + 1, M):
            nums[i], nums[j] = nums[j], nums[i]
            solve(c + 1)
            nums[i], nums[j] = nums[j], nums[i]


T = int(input())

for tc in range(1, T + 1):
    N, C = map(int, input().split())
    nums = []
    max_bonus = 0
    for n in str(N):
        nums.append(int(n))
    M = len(nums)
    check = set()

    solve(0)
    print(f'#{tc} {max_bonus}')
