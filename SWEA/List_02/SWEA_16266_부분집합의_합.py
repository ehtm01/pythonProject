# 16266. 2일차 - 부분집합의 합
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AYYk_zdayGUDFAVw&probBoxId=AZiB15-a_6bHBIT9&type=USER&problemBoxTitle=0807_List2&problemBoxCnt=4

T = int(input())

for tc in range(1, T+1):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = map(int, input().split())
    cnt = 0

    for i in range(1 << 12):
        num_lst = []
        for j in range(12):
            if i & (1 << j):
                num_lst.append(numbers[j])

        if len(num_lst) == N and sum(num_lst) == K:
            cnt += 1

    print(f'#{tc} {cnt}')
