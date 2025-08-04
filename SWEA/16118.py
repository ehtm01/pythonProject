T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    max_sum = 0
    min_sum = 0
    sum_num = 0
    # a[0]~a[M-1]까지를 더한 값인 max_num, min_num 설정
    for num in range(M):
        max_sum += a[num]
        min_sum += a[num]
    # 0부터 N - M까지 순회하는 i
    for i in range(N - M + 1):
        # sum_num: i부터 M개의 숫자를 더한 값
        for j in range(i, M + i):
            sum_num += a[j]
        if sum_num > max_sum:       # max_sum보다 크면
            max_sum = sum_num       # max_sum에 대입
        elif sum_num < min_sum:     # min_sum보다 작으면
            min_sum = sum_num       # min_sum에 대입

        sum_num = 0

    print(f'#{test_case} {max_sum - min_sum}')