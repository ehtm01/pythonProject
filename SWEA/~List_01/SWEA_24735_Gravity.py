N = int(input())
h = list(map(int, input().split()))

count_max = 0   # 상자 높이 최댓값이 중복일 때의 가짓수
max_box = 0     # 상자 높이 최댓값

for box in h:   # 상자 높이를 순회하여 반복
    if box > max_box:   # 상자 높이가 최댓값보다 클 때
        max_box = box   # 최댓값에 상자 높이 할당

high_box = h.index(max_box) # 최댓값의 인덱스로 어디서 떨어지는지 확인

for i in h:     # 상자 높이를 순회하여 반복
    if i == max_box:    # 상자 높이 최댓값이 몇 개나 있는지
        count_max += 1  # 카운트 증가

fall_height = N - count_max - high_box  
# 꼭대기에서 최댓값인 상자가 처음에 떨어지는 위치만큼 감소, 중복인 값만큼 또 감소시킴

print(fall_height)





