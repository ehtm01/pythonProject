# 9490. 풍선팡
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AXAerAPaVXMDFARP&probBoxId=AZh9Dhq6vtHHBINp&type=USER&problemBoxTitle=0806_List2&problemBoxCnt=9

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    max_sum = 0

    for i in range(N):
        paper_flower = list(map(int, input().split()))
        for j in range(M):
            arr[i][j] = paper_flower[j]

    for i in range(N):
        for j in range(M):
            center = arr[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                for dist in range(1, arr[i][j] + 1):
                    ni, nj = i + di * dist, j + dj * dist
                    if 0 <= ni < N and 0 <= nj < M:
                        center += arr[ni][nj]
            if max_sum < center:
                max_sum = center
    print(f'#{test_case} {max_sum}')
