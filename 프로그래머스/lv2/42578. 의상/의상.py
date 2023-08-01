def solution(clothes):
    answer = 1
    result = {}
    for cloth in clothes:
        if cloth[1] not in result:
            result[cloth[1]] = 1
        else:
            result[cloth[1]] += 1

    for c in result.values():
        answer *= (c+ 1)
    return answer - 1