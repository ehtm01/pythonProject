T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    Aj = list(map(int, input().split()))

    min_num = Aj[0]
    max_num = Aj[0]

    for j in Aj:
        if j > max_num:
            max_num = j
        elif j < min_num:
            min_num = j

    min_max = max_num - min_num

    print(f'#{test_case} {min_max}')
