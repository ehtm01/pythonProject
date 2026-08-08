from collections import deque

def solution(mats, park):
    # mats부터 내림차 순으로 정렬
    # 왼쪽부터 하나씩 크기를 비교해보며 완탐
    
    mats.sort(reverse=True)
    row = len(park)
    col = len(park[0])
    
    for mat in mats:
        r, c = row - mat + 1, col - mat + 1
        q = deque()
        
        for i in range(r):
            for j in range(c):
                if park[i][j] == "-1":
                    q.append((i, j))
        
        while q:
            y, x = q.popleft()
            corr = True

            for ny in range(y, y + mat):
                for nx in range(x, x + mat):
                    if park[ny][nx] != "-1":
                        corr = False
                        break
                if not corr:
                    break
            else:
                return mat
    
    return -1
                    