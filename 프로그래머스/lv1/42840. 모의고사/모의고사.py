def solution(answers):
    result = []
    score = [0, 0, 0]

    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx, answer in enumerate(answers):
        print(idx)
        if answer == std1[idx % len(std1)]:
            score[0] += 1
        if answer == std2[idx % len(std2)]:
            score[1] += 1
        if answer == std3[idx % len(std3)]:
            score[2] += 1

    for idx, num in enumerate(score):
        if num == max(score):
            result.append(idx+1)

    return result