# SWEA 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

passward = {'0001101': '0',
            '0011001': '1',
            '0010011': '2',
            '0111101': '3',
            '0100011': '4',
            '0110001': '5',
            '0101111': '6',
            '0111011': '7',
            '0110111': '8',
            '0001011': '9'
            }

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    deca_string = ''
    for r in range(N):
        for c in range(M - 1, -1, -1):
            if matrix[r][c] == '1':
                for j in range(c - 55, c + 1, 7):
                    deca_string += passward[matrix[r][j:j+7]]
                break
        if deca_string:
            break

    sum = result = 0
    for i in range(len(deca_string)):
        if i % 2 == 0:
            sum += int(deca_string[i]) * 3
        else:
            sum += int(deca_string[i])

    for n in deca_string:
        result += int(n)

    if sum % 10 == 0:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} 0')
