def solution(a, b):
    num = 2*a*b
    a, b = str(a), str(b)
    return max(int(a+b), num)