def solution(array, commands):
    answer = []
    for arr in commands:
        i = arr[0]
        j = arr[1]
        k = arr[2]
        tmp = sorted(array[i-1:j])
        answer.append(tmp[k-1])
    return answer