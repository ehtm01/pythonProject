# SWEA 24792. 정사각형 내부에 있는 정사각형의 개수
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AZh9PuJ6w2LHBINp&probBoxId=AZh9Dhq6vtHHBINp&type=USER&problemBoxTitle=0806_List2&problemBoxCnt=8

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [[0] * N for _ in range(N)]
    cnt = 1

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            for k in range(i, i + M):
                for a in range(j, j + M):
                    arr[k][a] = cnt
            cnt += 1

    print(f'#{test_case}')

    for result in arr:
        print(*result)
