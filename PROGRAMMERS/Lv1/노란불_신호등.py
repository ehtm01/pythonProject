import math

def solution(signals):
    answer = 0
    
    # 재귀로 들어간다?
    # 수열 규칙으로 보는게 제일 빠를거 같은데
    # test 1. 노란불 = (5n - 2) && (7n - 1)
    # => x % 5 = 3 and x % 7 = 6
    
    count = len(signals)
    lcm = 1     # 최소공배수 찾기
    
    for signal in signals:
        lcm = math.lcm(lcm, sum(signal))    # Python 3.9부터 가능
    
    array = [0] * lcm
        
    for signal in signals:
        length = sum(signal)
        for i in range(signal[0] + 1, signal[0] + signal[1] + 1):
            while i < len(array):
                array[i] += 1
                i += length
                
    for i, a in enumerate(array):
        if a == count:
            answer = i
            break
    else:
        answer = -1    
    return answer