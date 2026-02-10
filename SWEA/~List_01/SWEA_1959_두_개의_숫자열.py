def solve():
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    sum1 = 0

    if N > M:
        move = N - M + 1
        for i in range(move):
            sum2 = 0
            for j in range(M):
                sum2 += Ai[i + j] * Bj[j]
        
            if sum2 > sum1:
                sum1 = sum2
        return sum1
    else:
        move = M - N + 1
        for i in range(move):
            sum2 = 0
            for j in range(N):
                sum2 += Ai[j] * Bj[i + j]
        
            if sum2 > sum1:
                sum1 = sum2
        return sum1

T = int(input())

results = []

for test_case in range(1, T + 1):
    result = solve()
    results.append(f'#{test_case} {result}')

for value in results:
    print(value)