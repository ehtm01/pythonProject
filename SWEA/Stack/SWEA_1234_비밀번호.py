# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
T = 10

for tc in range(1, T+1):
    N, M = map(str, input().split())
    top = -1
    s = [''] * int(N)

    for i in M:
        top += 1
        s[top] = i
        if s[top] == s[top-1]:
            top -= 2

    print(f'#{tc} {"".join(map(str, s[:top+1]))}')
