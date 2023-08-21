import itertools
import math


def check_num(num):
    end = int(math.sqrt(num))
    for i in range(2, end + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    data = itertools.combinations(nums, 3)
    for ele in data:
        if check_num(sum(ele)):
            answer += 1
    return answer
