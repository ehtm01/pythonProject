# SWEA 16943. 4일차 응용 - 이진 탐색
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_lst = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    cnt = 0

    arr = sorted(N_lst)

    def bs(t):
        global cnt

        l = prev = 0
        r = N - 1

        while l <= r:
            mid = (l + r) // 2

            if arr[mid] == t:
                cnt += 1
                return

            if t < arr[mid]:
                if prev == 1:
                    return
                r = mid - 1
                prev = 1
            else:
                if prev == -1:
                    return
                l = mid + 1
                prev = -1

    for num in nums:
        bs(num)

    print(f'#{tc} {cnt}')
