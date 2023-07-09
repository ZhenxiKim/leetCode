import sys

n = int(sys.stdin.readline())

for i in range(n):
    star = "*"
    for j in range(i):
        star += "*"
    print(star)