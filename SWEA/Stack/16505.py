# 16505. 4일차 - 종이붙이기
def paper(N):
    n = int(N / 10)
    f = [0] * (n + 1)
    f[0] = 1
    f[1] = 3
    for i in range(2, n):
        if i % 2 == 0:
            f[i] = 2 * f[i-1] - 1
        else:
            f[i] = 2 * f[i-1] + 1

    return f[n - 1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {paper(N)}')
