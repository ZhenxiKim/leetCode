import math

def solution(numer1, denom1, numer2, denom2):
    number = (numer1 * denom2) +(numer2 * denom1) 
    denom  = (denom1 * denom2)
    gcd = math.gcd(number, denom)
    return [number//gcd, denom//gcd]  