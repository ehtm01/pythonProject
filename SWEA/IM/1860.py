# 1860. 진기의 최고급 붕어빵
T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    # sec = list(map(int, input().split()))
    # max_t = max(sec)
    # bread = [0] * (max_t + 1)
    # result = 'Possible'
    # sec.sort()
    #
    # for m in range(len(bread)):
    #     if (m + 1) % M == 0:
    #         bread[m] = K
    #
    # for t in sec:
    #     for i in range(t):
    #         if bread[i]:
    #             bread[i] -= 1
    #             break
    #     else:
    #         result = 'Impossible'
    #
    #     if result == 'Impossible':
    #         break
    #
    # print(f'#{tc} {result}')

    # 손님 도착 시간 리스트 정렬
    arrivals = sorted(map(int, input().split()))
    result = 'possible'
    # 손님이 t에 왔을 때 그 때까지 만든 빵 수
    for i, t in enumerate(arrivals):
        stack_bread = (t // M) * K
    # 필요한 빵 수
        if stack_bread < i + 1:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')
