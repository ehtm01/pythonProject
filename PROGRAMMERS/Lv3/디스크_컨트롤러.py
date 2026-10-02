from heapq import heappop, heappush

def solution(jobs):
    answer = 0
    req = []
    prq = []
    
    # 대기 큐: 작업 번호, 작업 요청 시각, 작업 소요 시간 저장
    # 디스크 컨트롤러: 하드디스크 작업 X + 대기 있음 -> 우선순위 높은 작업 시작
    # 우선순위: 소요시간 짧음, 요청 시각 빠름, 작업 번호 작음
    # 작업은 끝날 때까지 수행
    # 작업을 마치는 시점과 요청이 들어오는 시점이 겹치면 작업 꺼내기 전에 대기 큐로 넣음
    
    # 큐를 두 개 잡는다 -> 요청 대기 큐, 작업 큐
    
    for idx, j in enumerate(jobs):
        heappush(req, (j[0], j[1], idx))
        
    t = 0
    
    while req or prq:
        while req and req[0][0] <= t:  
            temp = heappop(req)
            heappush(prq, (temp[1], temp[0], temp[2]))
        
        if prq:
            temp = heappop(prq)
            t += temp[0]
            answer += t - temp[1]
        else:
            t = req[0][0]
            
    answer //= len(jobs)
    
    return answer