import sys

N, B = map(int, sys.stdin.readline().split())
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ''
while N != 0:
    result += str(tmp[N % B])
    N = N // B

print(result[::-1])
