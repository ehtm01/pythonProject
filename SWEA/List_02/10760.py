# 10760. 우주선착륙2
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AXSHJueab1oDFAQT&probBoxId=AZiB15-a_6bHBIT9&type=USER&problemBoxTitle=0807_List2&problemBoxCnt=6

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Aij = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(M):
            center = Aij[i][j]
            candi_cnt = 0
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    if Aij[ni][nj] < center:
                        candi_cnt += 1

            if candi_cnt >= 4:
                result.append(center)

    print(f'#{tc} {len(result)}')
