from collections import deque

def solution(arr):
    q = deque()
    for num in arr:
        if not q:
            q.append(num)
        else:
            x = q.pop()
            q.append(x)
            if x != num:
                q.append(num)
                
    return list(q)