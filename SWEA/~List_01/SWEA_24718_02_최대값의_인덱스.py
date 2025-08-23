T = int(input())

for test_case in range(1, T+1):
    case = int(input())  # 테스트 케이스 입력
    num_lst = list(map(int, input().split()))  # N개의 숫자 입력
    max_num = num_lst[0]    # max_num의 기본값 설정

    for num in num_lst:  # num_lst 순회하여 반복
        if num > max_num:   # 최댓값 초과 시
            max_num = num   # max_num에 할당

    print(f'#{test_case} {max_num} {num_lst.index(max_num)}')   # 인덱스까지 출력
