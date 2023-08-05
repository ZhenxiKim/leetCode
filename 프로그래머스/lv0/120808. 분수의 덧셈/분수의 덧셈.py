import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    gcd_num = math.gcd(denom, numer)
    answer.append(numer / gcd_num)
    answer.append(denom / gcd_num)
    return answer