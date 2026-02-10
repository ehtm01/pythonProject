# 16312. 2일차 - 이진탐색
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AYYqKXCKE6gDFAVw&probBoxId=AZiB15-a_6bHBIT9&type=USER&problemBoxTitle=0807_List2&problemBoxCnt=6


def binarySearch(P, key):
    start = 1
    end = P
    cnt = 0
    while start <= end:
        cnt += 1
        middle = int((start + end) / 2)
        if middle == key:
            return cnt
        elif middle > key:
            end = middle
        else:
            start = middle

    return cnt


T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnt_a = binarySearch(P, Pa)
    cnt_b = binarySearch(P, Pb)

    if cnt_a < cnt_b:
        winner = 'A'
    elif cnt_b < cnt_a:
        winner = 'B'
    else:
        winner = '0'
    print(f'#{tc} {winner}')
