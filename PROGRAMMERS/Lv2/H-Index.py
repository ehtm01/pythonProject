# 첫 풀이

def solution(citations):
    answer = 0
    
    # 논문 n편 중 h번 이상 인용된 논문이 h편 이상, 나머지 논문이 h번 이하 인용된 h의 최댓값 -> H-Index
    
    for h in range(1, len(citations) + 1):
        c = sum(x >= h for x in citations)
        if c >= h:
            answer = h
        else:
            break
    
    return answer

# 수정 풀이

def solution(citations):
    answer = 0
    
    c = sorted(citations, reverse=True)
    for idx, ci in enumerate(c):
        if ci >= idx + 1:
            answer = idx + 1
        else:
            break
    
    return answer