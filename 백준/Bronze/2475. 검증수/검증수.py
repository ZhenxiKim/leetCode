import sys

data = list(sys.stdin.readline().split())
sum = 0
for i in data:
    sum += int(i) * int(i)

print(sum % 10)
