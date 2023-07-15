def solution(numbers):
    answer = []
    for idx, num in enumerate(numbers):
        for j in range(idx +1, len(numbers)):
            value = num + numbers[j]
            if value not in answer:
                answer.append(value)
    return sorted(answer)