T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a_i = list(map(int, input().split()))
    max_idx = 0
    min_idx = 0

    for i in range(N):
        if a_i[i] >= a_i[max_idx]:
            max_idx = i
            continue
        elif a_i[i] < a_i[min_idx]:
            min_idx = i

    result = max_idx, min_idx
    result = sorted(result)

    print(f'#{test_case} {result[1] - result[0]}')