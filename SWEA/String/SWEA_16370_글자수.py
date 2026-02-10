# 16370. 3일차 - 글자수
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AYY0cqzKavoDFAVw&probBoxId=AZiHADjae2zHBINp&type=USER&problemBoxTitle=0808_String&problemBoxCnt=2

T = int(input())

for tc in range(1, T+1):
    N = list(input())
    M = list(input())
    max_cnt = 0

    for i in range(len(N)):
        if N[i] in M:
            cnt = M.count(N[i])
            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{tc} {max_cnt}')
