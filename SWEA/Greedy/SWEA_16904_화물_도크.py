# SWEA 16904. 3일차 응용 - 화물 도크
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    time = [[0] for _ in range(N)]
    for t in range(N):
        s, e = map(int, input().split())
        time[t] = [e, s]

    time.sort()
    cnt = 0
    def dock(idx):
        global cnt

        if time[idx]:
            cnt += 1

        if idx >= N - 1:
            return

        for i in range(idx + 1, N):
            if time[i] and time[idx][0] > time[i][1]:
                time[i] = 0

        x = idx + 1
        while x < N - 1:
            if time[x]:
                break
            else:
                x += 1

        dock(x)

    dock(0)
    print(f'#{test_case} {cnt}')
