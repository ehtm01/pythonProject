T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a = b = c = d = e = 0
    while N % 2 == 0:   # 2로 나눈 나머지가 없으면 반복
        N /= 2
        a += 1

    while N % 3 == 0:   # 3으로 나눈 나머지가 없으면 반복
        N /= 3
        b += 1

    while N % 5 == 0:   # 5로 나눈 나머지가 없으면 반복
        N /= 5
        c += 1

    while N % 7 == 0:   # 7로 나눈 나머지가 없으면 반복
        N /= 7
        d += 1

    while N % 11 == 0:  # 11로 나눈 나머지가 없으면 반복
        N /= 11
        e += 1

    print(f'#{test_case} {a} {b} {c} {d} {e}')

