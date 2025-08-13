# SWEA 16268. 풍선팡2
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AYYlGU56XOkDFARc&probBoxId=AZh9Dhq6vtHHBINp&type=USER&problemBoxTitle=0806_List2&problemBoxCnt=8

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    max_sum = 0

    for i in range(N):
        paper_flower = list(map(int, input().split()))
        for j in range(len(paper_flower)):
            arr[i][j] = paper_flower[j]

    for i in range(N):
        for j in range(M):
            center = arr[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    center += arr[ni][nj]
            if max_sum < center:
                max_sum = center
    print(f'#{test_case} {max_sum}')

