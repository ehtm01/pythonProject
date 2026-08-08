def solution(wallet, bill):
    # 예를 들어 지갑의 크기가 30 * 15이고 지폐의 크기가 26 * 17이라면 한번 반으로 접어 13 * 17 크기로 만든 뒤 90도 돌려서 지갑에 넣을 수 있습니다.
    # 지폐를 접을 때는 항상 길이가 긴 쪽을 반으로 접습니다.
    # 접기 전 길이가 홀수였다면 접은 후 소수점 이하는 버립니다. (bill[0] // 2)
    # 접힌 지폐를 그대로 또는 90도 돌려서 지갑에 넣을 수 있다면 그만 접습니다.
    count = 0
    
    while True:
        if max(bill) <= max(wallet) and min(bill) <= min(wallet):
            return count
        
        if bill[0] >= bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        
        count += 1