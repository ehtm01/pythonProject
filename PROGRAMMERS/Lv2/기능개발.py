def solution(progresses, speeds):
    answer = []
    while progresses:
        if len(progresses) == 1:
            answer.append(1)
            break
            
        days = (100 - progresses[0]) // speeds[0] if (100 - progresses[0]) % speeds[0] == 0 else ((100 - progresses[0]) // speeds[0]) + 1
        for i, p in enumerate(progresses):
            p += days * speeds[i]
            progresses[i] = p
        
        count = 0
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            if not progresses:
                break
            
        answer.append(count)
    
    return answer