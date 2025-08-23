def baseball():
    N, K = map(int, input().split())    # 야구선수 인원, 허용 가능한 실력 입력
    stat = list(map(int, input().split()))  # 야구선수들의 실력 입력

    stat.sort()  # 오름차순으로 정렬
    left = 0
    max_len = 0

    for right in range(N):  # 야구선수 인원만큼 순회하여 right 인덱스 반복
        while stat[right] - stat[left] > K:  # left 인덱스와 right 인덱스 아구선수의 실력 차이가 K보다 크면 반복
            left += 1   # left 인덱스 오른쪽으로 한 칸 이동
        numbers = right - left + 1  # 아구선수의 실력 차이가 K보다 크지 않으면 인원수 저장
        if numbers > max_len:   # 최대 인원수보다 지금 인원수가 크면
            max_len = numbers   # 최대 인원수 갱신

    return max_len  # 결과 출력


""" 
만약 6 4 2 3 의 실력을 가진 야구선수들이 입력된다면 2 3 4 6 으로 오름차순 정렬되고,
right = 0, left = 0부터 시작한다.
2 - 2 < 2 이므로
numbers = 2 - 2 + 1 = 1명
max_len = 0이므로 max_len = 1로 갱신
3 - 2 < 2, numbers = 2, max_len = 2
4 - 2 = 2, numbers = 3, max_len = 3
6 - 2 > 2, left = 1
6 - 3 = 3, left = 2
6 - 4 = 2, numbers = 3 - 2 + 1 = 2 < max_len
결국 max_len = 3이 출력된다 (2 3 4 인원끼리 팀을 하는 것)
"""

results = []
T = int(input())
for test_case in range(1, T + 1):
    result = baseball()
    results.append(f'#{test_case} {result}')

for result in results:
    print(result)
