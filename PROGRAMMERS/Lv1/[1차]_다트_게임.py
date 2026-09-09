def solution(dartResult):
    # 3번의 기회
    # 각 기회에서 얻을 수 있는 점수: 0 ~ 10
    # S: ^1, D: ^2, T: ^3 => 점수마다 하나씩 존재
    # *: 해당 + 직전 점수 2배, #: 해당 점수 감점 => 점수마다 둘 중 하나만 존재
    # *: 첫 번째 가능, 중첩 가능(*, #)
    
    # 파싱용 위치 변수
    start = 0
    end = 1
    
    # 점수 저장 변수
    num = 0
    
    # 직전에 얻은 점수 변수
    prev = 0
    
    # 결과값
    result = 0
    
    # 파싱용 숫자 리스트
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for i, n in enumerate(dartResult):
        # 만약 i가 start보다 작으면 넘어감(10 대비)
        if i < start:
            continue
        
        # n이 정수이면
        if n in nums:
            # print(result)
            result += prev
            prev = num
            # n이 1이면 숫자 10인지 뒷 문자 확인
            if n == '1' and dartResult[i + 1] == '0':
                end += 1
            num = int(dartResult[start:end])
            
        elif n == 'D':
            num **= 2
        
        elif n == 'T':
            num **= 3
            
        elif n == '*':
            prev *= 2
            num *= 2
        
        elif n == '#': 
            num = -num
            
        start = end
        end += 1
        
    result += num
    result += prev
    
    return result