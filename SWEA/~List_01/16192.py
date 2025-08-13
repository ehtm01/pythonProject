T = int(input())

for test_case in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    charge = list(map(int, input().split()))
    # N+1 개의 정류장 배열 생성
    arr = [0] * (N+1)
    # M개의 충전기를 배열에 1로 할당
    for i in range(M):
        arr[charge[i]] += 1

    curr_loca = 0   # 현재 위치
    char_cnt = 0    # 충전 횟수

    for j in range(1, M):
        # 만약 충전소간의 거리가 K보다 크면
        if charge[j] - charge[j-1] > K:
            char_cnt = 0
            break
    else:
        # 현재 위치가 N-K 미만이면 반복
        while curr_loca < N-K:
            # 1, 2, 3, ..., K 까지 이동거리가 순회하며 반복
            for distance in range(1, K+1):
                # 현재 위치에 이동 거리를 더한 곳에 충전기가 있으면
                if arr[curr_loca + distance]:
                    # 최대 이동거리로 저장
                    max_dist = distance
            
            char_cnt += 1   # 충전 횟수 1 증가
            curr_loca += max_dist   # 현재 위치에 최대 이동거리 저장

    print(f'#{test_case} {char_cnt}')
