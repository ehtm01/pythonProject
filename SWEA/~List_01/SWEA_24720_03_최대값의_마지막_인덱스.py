T = int(input())

for test_case in range(1, T+1):
    case = int(input())  # 테스트 케이스 입력
    num_lst = list(map(int, input().split()))  # N개의 숫자 입력
    max_num = num_lst[0]    # max_num의 기본값 설정

    for i in range(len(num_lst)):  # num_lst의 길이를 범위로 순회하며 반복
        if num_lst[i] >= max_num:   # 최댓값 이상일 때
            max_num_index = i   # i를 인덱스로 저장
            max_num = num_lst[i]   # 최댓값을 max_num에 할당

    print(f'#{test_case} {max_num} {max_num_index}')   # 마지막 최댓값의 인덱스까지 출력
