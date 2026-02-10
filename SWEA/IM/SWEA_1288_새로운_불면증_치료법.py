# 1288. 새로운 불면증 치료법
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = []
    K = N

    while True:
        for n in str(N):
            num_lst.append(n)
        if len(set(num_lst)) == 10:
            break
        N += K

    print(f'#{tc} {N}')
