# 2005. 파스칼의 삼각형
T = int(input())

for t in range(1, T+1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    results = []

    for i in range(N):
        matrix[i][0] = 1
        if N > 1 and i > 0:
            for j in range(i):
                matrix[i][j+1] = matrix[i-1][j] + matrix[i-1][j+1]
        results.append(matrix[i][:i+1])

    print(f'#{t}')
    for result in results:
        print(' '.join(map(str, result)))
