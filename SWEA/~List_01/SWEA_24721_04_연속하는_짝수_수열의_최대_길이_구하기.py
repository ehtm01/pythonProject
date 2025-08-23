T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))

    # example_1
    """ max_len = 0

    for left in range(N):
        if num_lst[left] % 2 == 0:
            len_lst = []
            for right in range(left, N):
                if num_lst[right] % 2 == 0:
                    len_lst.append(num_lst[right])
                    if len(len_lst) > max_len:
                        max_len = len(len_lst)
                else:
                    len_lst = [] """

    # example_2
    """ sequence_lst = []
    even_num = []

    for num in num_lst:
        if num % 2 == 0:
            even_num.append(num)
        else:
            if even_num:
                sequence_lst.append(even_num)
                even_num = []

    if even_num:
        sequence_lst.append(even_num)

    try:
        max_len = max(
            [
                len(sequence_lst[i]) for i in range(len(sequence_lst))
            ]
        )
    except ValueError:
        max_len = 0"""
    # max(lengths, default=0)이 더 간결함

    # example_3
    lst_len = 0
    max_len = 0

    for num in num_lst:
        if num % 2 == 0:
            lst_len += 1
            if lst_len > max_len:
                max_len = lst_len
        else:
            lst_len = 0

    print(f'#{test_case} {max_len}')
