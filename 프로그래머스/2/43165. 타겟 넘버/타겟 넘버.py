def bfs(idx, sum_val, numbers, target):
    global answer
    if idx == len(numbers):
        if sum_val == target:
            answer += 1
        return
    bfs(idx + 1, sum_val + numbers[idx], numbers, target)
    bfs(idx + 1, sum_val - numbers[idx], numbers, target)


def solution(numbers, target):
    global answer
    answer = 0
    bfs(0, 0, numbers, target)  # index, sum
    return answer