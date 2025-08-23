T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))

    prev_num = None  # 이전 숫자로 None 할당
    max_len = 0  # 최대 길이 0 할당
    sequence_len = 0    # 연속된 길이 0 할당

    for num in num_lst:  # 양의 정수로 이루어진 수열을 순회하며 반복
        if num % 2 == 0:    # 양의 정수가 짝수일 때
            if prev_num is not None and num > prev_num:  # 이전 숫자가 None이 아니면서 양의 정수보다 작으면
                sequence_len += 1   # 연속된 길이 1 증가
            else:   # 이전 숫자가 None이거나 양의 정수보다 크면
                sequence_len = 1    # 연속된 길이 1로 초기화
            prev_num = num  # 이전 숫자를 짝수인 현재 양의 정수로 변경
            # 최대 길이와 연속된 길이 중 큰 값을 최대 길이로 할당
            max_len = max(sequence_len, max_len)
        else:   # 양의 정수가 홀수일 때
            prev_num = None  # 이전 숫자는 None으로 초기화

    print(f'#{test_case} {max_len}')
