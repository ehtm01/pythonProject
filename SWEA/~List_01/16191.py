T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a_i = list(map(int, input().strip()))

    cnt = [0] * 10      # 0~9 1차원 배열 생성

    for i in range(N):  # N개의 숫자에 대해서
        cnt[a_i[i]] += 1    # 숫자 크기에 할당되는 1차원 배열 위치 + 1

    max_num = 0
    num_index = 0

    for j in range(len(cnt)):
        if cnt[j] >= max_num:   # 카드 장수가 같으면 적힌 숫자가 큰 쪽을 출력
            max_num = cnt[j]
            num_index = j

    print(f'#{test_case} {num_index} {max_num}')
