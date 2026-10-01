def solution(prices):
    answer = len(prices) * [0]
    stack = [0]

    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            x = stack.pop()
            answer[x] = i - x
        stack.append(i)
    while stack:
        k = stack.pop()
        answer[k] = len(prices) - 1 - k

    return answer
