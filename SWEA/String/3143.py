# 3143. 가장 빠른 문자열 타이핑
T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split())
    N, M = len(A), len(B)
    cnt = N
    i = 0

    while i < N:
        if i + M > N:
            break
        if A[i:i+M] == B:
            cnt -= M - 1
            i += M
        else:
            i += 1


    print(f'#{tc} {cnt}')
