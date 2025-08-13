T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().strip()))
    # 기본 카운트 = 1
    cnt = 1     
    max_cnt = 1
    for i in range(N-1):    # N-1 까지 순회하며 반복
        if arr[i] == arr[i+1] == 1:     # arr[i]와 다음 요소가 1이면
            cnt += 1    # 카운트 1 증가
            # max_cnt 갱신
            if cnt > max_cnt:   
                max_cnt = cnt
        # 아니면 cnt 초기화
        else:
            cnt = 1

    print(f'#{test_case} {max_cnt}')