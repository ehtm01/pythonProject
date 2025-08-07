# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
# https://swexpertacademy.com/main/talk/solvingClub/problemPassedUser.do?contestProbId=AV14ABYKADACFAYh&solveclubId=AZhdubEaIe3HBIT9&problemBoxTitle=0807_List2&problemBoxCnt=6&probBoxId=AZiB15-a_6bHBIT9

# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for j in range(100):
        if ladder[0][j] == 1:
            x, y = j, 0
            while y < 99:
                if x+1 < 100 and ladder[y][x+1] == 1:
                    while x+1 < 100 and ladder[y][x+1] == 1:
                        x += 1
                elif x-1 >= 0 and ladder[y][x-1] == 1:
                    while x-1 >= 0 and ladder[y][x-1] == 1:
                        x -= 1
                y += 1

            if ladder[y][x] == 2:
                result = j

    print(f'#{tc} {result}')
