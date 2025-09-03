# SWEA 16788. 이진수2
T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    t = 1
    bin = ''

    while N > 0:
        if t >= 13:
            print(f'#{tc} overflow')
            break
        if N >= 2 ** (-t):
            N -= 2 ** (-t)
            bin += '1'
        else:
            bin += '0'
        t += 1
    else:
        print(f'#{tc} {bin}')
