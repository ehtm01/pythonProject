# 1966. 숫자를 정렬하자
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PrmyKAWEDFAUq&categoryId=AV5PrmyKAWEDFAUq&categoryType=CODE&problemTitle=1966&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    # 버블 정렬 실행
    for last in range(N-1, 0, -1):
        for i in range(last):
            if num[i] > num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]

    print(f"#{test_case} {' '.join(map(str, num))}")
    # ' '.join: 'iterable'에 담긴 문자열들을 ' '로 이어 붙여 하나의 큰 문자열로 만듦
    # map(str, num): 'iterable'인 num의 각 원소에 str()을 적용한 결과를 차례대로 반환