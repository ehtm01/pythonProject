# 1954. 달팽이 숫자
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AV5PobmqAPoDFAUq&probBoxId=AZiB15-a_6bHBIT9&type=PROBLEM&problemBoxTitle=0807_List2&problemBoxCnt=4
T = int(input())


def odd_cal(n):
    k = 0
    m = 0
    while n >= 3:
        for a in range(1, n + 1):
            matrix[k][a + k - 1] = a + m
        for a in range(1, n):
            matrix[a + k][n - 1 + k] = n + a + m
        for a in range(1, n):
            matrix[n - 1 + k][n - a - 1 + k] = n + a + (n - 1) + m
        for a in range(1, n - 1):
            matrix[n - a - 1 + k][k] = n + a + 2 * (n - 1) + m
        m = int(8 * (n - 1) / 2)
        n -= 2
        k += 1


def even_cal(n):
    k = 0
    m = 0
    while n >= 2:
        for a in range(1, n + 1):
            matrix[k][a + k - 1] = a + m
        for a in range(1, n):
            matrix[a + k][n - 1 + k] = n + a + m
        for a in range(1, n):
            matrix[n - 1 + k][n - a - 1 + k] = n + a + (n - 1) + m
        for a in range(1, n - 1):
            matrix[n - a - 1 + k][k] = n + a + 2 * (n - 1) + m
        m = int(8 * n / 2 - 4)
        n -= 2
        k += 1


for tc in range(1, T+1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]

    if N % 2 == 1:
        matrix[int((N - 1) / 2)][int((N - 1) / 2)] = N ** 2
        odd_cal(N)

    if N % 2 == 0:
        even_cal(N)

    print(f'#{tc}')
    for result in matrix:
        print(' '.join(map(str, result)))
