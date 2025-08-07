# 16312. 2일차 - 이진탐색
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AYYqKXCKE6gDFAVw&probBoxId=AZiB15-a_6bHBIT9&type=USER&problemBoxTitle=0807_List2&problemBoxCnt=6

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    book_lst = list(map(int, range(P)))
    start = 0
    end = P - 1
    result = []

    while start <= end:
        middle = (start + end) // 2
        if book_lst[middle] == Pa:
            result.append(book_lst[middle])
        elif book_lst[middle] > Pa:
            end = middle - 1
        else:
            start = middle + 1



