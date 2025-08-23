""" def solve():

    N = int(input())
    a = []
    for i in range(N):
        a.append(input().split())

    outline = []

    for k in range(N):
        line = ""
        for j in range(N):
            line += a[N - j - 1][k]
        line += " "
        for j in range(N):
            line += a[N - k - 1][N - j - 1]  
        line += " "
        for j in range(N):
            line += a[j][N - k -1]
        outline.append(line)
    return "\n".join(outline)

T = int(input())
results = []

for test_case in range(1, T+1):
    result = solve()
    results.append(f'#{test_case}\n{result}')

print('\n'.join(results)) """
