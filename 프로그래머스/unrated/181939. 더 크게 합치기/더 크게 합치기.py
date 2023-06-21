def solution(a, b):
    answer1 = str(a) + str(b)
    answer2 = str(b) + str(a)
    if int(answer1) > int(answer2):
        return int(answer1)
    else:
        return int(answer2)