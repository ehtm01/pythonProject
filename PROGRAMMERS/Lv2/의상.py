def solution(clothes):
    closet = dict()
    for name, kind in clothes:
        closet[kind] = closet.get(kind, 0) + 1
        
    result = 1
    for v in closet.values():
        result *= (v + 1)
    return result - 1