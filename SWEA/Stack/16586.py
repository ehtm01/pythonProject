# 16586. 5일차 - 배열 최소 합
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 초기 비교 대상을 matrix 의 대각선 방향 값으로 잡는다.
    min_sum = 0
    for n in range(N):
        min_sum += matrix[n][n]
    row = list(range(N))


    def back_track(idx, sum_num):
        global min_sum

        if idx == N:
            if min_sum > sum_num:
                min_sum = sum_num
                return
        if min_sum <= sum_num:
            return

        for c in range(idx, N):
            row[idx], row[c] = row[c], row[idx]
            back_track(idx + 1, sum_num + matrix[row[idx]][idx])
            # col 원상 복구
            row[idx], row[c] = row[c], row[idx]


    back_track(0, 0)
    print(f'#{tc} {min_sum}')
