import sys

read = list(map(int, sys.stdin.readline().split()))
normal = [1,1,2,2,2,8]
for i in range(len(read)):
    print(normal[i] - read[i], end=' ')