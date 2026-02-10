# BAEK 22251. 빌런 호석
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# N: 최대 층 수, K: LED 칸 수, P: 최대 반전 횟수, X: 현재 층 수
N, K, P, X = map(int, input().split())

# 숫자를 전부 표현하면 되지 않을까
zero = [True, True, True, False, True, True, True]
one = [False, False, True, False, False, True, False]
two = [True, False, True, True, True, False, True]
three = [True, False, True, True, False, True, True]
four = [False, True, True, True, False, True, False]
five = [True, True, False, True, False, True, True]
six = [True, True, False, True, True, True, True]
seven = [True, False, True, False, False, True, False]
eight = [True, True, True, True, True, True, True]
nine = [True, True, True, True, False, True, True]

print(zero)

