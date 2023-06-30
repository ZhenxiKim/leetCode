import math

n = int(input())
data = list(map(int, input().split()))
# 소수 판별 제곱근까지
cnt = 0


def is_prime_number(x):
    if x != 1:
        for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
        return True


for i in data:
    result = is_prime_number(i)
    if result == True:
        cnt += 1
print(cnt)
