def solution(n, w, num):    
    # w 만큼 상자를 먼저 쌓고 지그재그로 누적해서 쌓는다
    # 꺼내려는 상자 번호가 주어지면 그 위에 누적된 상자가 몇 개인지 알고 싶음
    # 리스트에 숫자를 더하는게 좋으려나? dp처럼
    box_count = [0] * (n + 1)

    for i in range(w, n):                               # 몫을 활용해서 위치를 구하기 위해 인덱스를 하나씩 낮춤
        under_floor = i // w                            # 아래에 몇 층이 있는지 계산
        
        while under_floor > 0:                          # 아래 층이 있을 때 반복
            box_count[w * under_floor - i % w] += 1     # 바로 아래 층에서 끝나는 숫자에 현재 위치 번호를
                                                        # w로 나눈 나머지 값을 빼면 바로 아래 층 번호가 나옴
                                                        # 그 곳의 값을 증가시키고
            i = w * under_floor - i % w - 1             # 다음 인덱스로 활용하기 위해 1을 빼줌
            under_floor -= 1                            # 층이 줄었으니 아래 층 개수도 줄임
            
    return box_count[num] + 1                           # 꺼내는 박스 위의 것 + 박스 자신 개수 더함