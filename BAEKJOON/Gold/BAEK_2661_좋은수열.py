# BAEK 2661. 좋은 수열
import sys
sys.stdin = open('input.txt', 'r')


def backtrack(cnt):
    a = len(ans)
    if a % 2 == 1:
        for i in range(a - 1, (a // 2), -1):
            if ans[i:] == ans[i*2-a:i]:
                return
    else:
        for i in range(a - 1, (a // 2) - 1, -1):
            if ans[i:] == ans[i*2-a:i]:
                return

    if cnt == N:
        b = ''.join(map(str, ans))
        print(b)
        return True

    for i in range(1, 4):
        ans.append(i)
        if backtrack(cnt + 1):
            return True
        ans.pop()


N = int(input())
ans = []

backtrack(0)
