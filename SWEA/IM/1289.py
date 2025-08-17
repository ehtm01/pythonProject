# 1289. 원재의 메모리 복구하기
T = int(input())

for tc in range(1, T+1):
    bit = list(map(int, input().strip()))
    reset = [0] * len(bit)
    cnt = 0

    for i in range(len(bit)):
        if reset[i] != bit[i]:
            for n in range(i, len(bit)):
                reset[n] = bit[i]
            cnt += 1

    print(f'#{tc} {cnt}')
