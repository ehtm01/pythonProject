# 1959. 두 개의 숫자열
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    diff = abs(N - M)
    max_sum = 0
    if N > M:
        Aj, Bj = Bj, Aj
        N, M = M, N

    for d in range(M - N + 1):
        sum_num = 0
        for i in range(N):
            sum_num += Aj[i] * Bj[d + i]
        max_sum = max(max_sum, sum_num)

    print(f'#{tc} {max_sum}')
