import itertools
import math


def check_num(num):
    middle = int(math.sqrt(num))
    for i in range(2, middle + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    candidate = set()
    num_list = []
    for i in range(len(numbers)):
        num_list.append(numbers[i])

    for i in range(1, len(numbers) + 1):
        numbers = set(map(int, map(''.join, itertools.permutations(num_list, i))))
        candidate |= numbers

    cnt = 0
    for num in candidate:
        if num not in [0,1]:
            if check_num(num):
                cnt += 1
    return cnt

