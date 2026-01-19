# BAEK 15918. 랭퍼든 수열쟁이야!!
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

# 랭퍼드 수열
# 1. 1 이상 n 이하의 자연수가 각각 두 개씩 들어 있다.
# 2. 두 개의 1 사이에는 정확히 1개의 수가 있다.
# 3. 두 개의 2 사이에는 정확히 2개의 수가 있다.
# 4. ...
# 5. 두 개의 n 사이에는 정확히 n개의 수가 있다.
# x번째 수와 y번째 수는 같다는 조건

n, x, y = map(int, input().split())

"""
3 x x x 3 x

7 x x y x x x x 7 y x x x x

y 12 y x x x x x x x x x 12 x x x x x x x x x x x
"""

fix = y - x - 1
array = [0] * (2 * n + 1)
array[x] = array[y] = fix
visited = [False] * (n + 1)
visited[fix] = True
result = 0

def backtrack(cnt):
    global result
    if cnt == 2 * n + 1:
        result += 1
        return
    if array[cnt]:
        backtrack(cnt + 1)
    else:
        for x in range(n + 1):
            if not visited[x] and cnt + x + 1 < 2 * n + 1 and array[cnt + x + 1] == 0:
                array[cnt] = array[cnt + x + 1] = x
                visited[x] = True
                backtrack(cnt + 1)
                visited[x] = False
                array[cnt] = array[cnt + x + 1] = 0

backtrack(1)
print(result)
