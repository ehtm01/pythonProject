from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville) >= 2:
        if scoville[0] < K:
            heappush(scoville, heappop(scoville) + 2 * heappop(scoville))
            answer += 1
        else:
            break
            
    if scoville[0] < K:
        answer = -1
            
    return answer