def solution(lines):
    data = [0] * 200
    for arr in lines:
        for i in range(arr[0] + 100, arr[1] + 100):
            data[i] += 1

    answer = 0
    for j in data:
        if j > 1:
            answer += 1
    return answer
