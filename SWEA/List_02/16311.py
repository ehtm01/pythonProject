# 16311. 2일차 - 특별한 정렬
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AYYqJ3jqE0EDFAVw&probBoxId=AZiB15-a_6bHBIT9&type=USER&problemBoxTitle=0807_List2&problemBoxCnt=4

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))

    for i in range(N-1):
        min_idx = i
        max_idx = i
        for j in range(i+1, N):
            if num_lst[min_idx] > num_lst[j]:
                min_idx = j
            if num_lst[max_idx] < num_lst[j]:
                max_idx = j
        if i % 2 == 0:
            num_lst[i], num_lst[max_idx] = num_lst[max_idx], num_lst[i]
        else:
            num_lst[i], num_lst[min_idx] = num_lst[min_idx], num_lst[i]

    print(f'#{tc} {" ".join(map(str, num_lst[:10]))}')
