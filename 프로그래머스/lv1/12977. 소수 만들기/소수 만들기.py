import math
from itertools import combinations

def check_num(num):
    end = int(math.sqrt(num))
    for i in range(2, end + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    data = list(combinations(nums,3)) #중복을 허용하지 않고 순서가 의미있는 조합
    for element in data:
        result = check_num(sum(element))
        if result:
            answer += 1
    return answer