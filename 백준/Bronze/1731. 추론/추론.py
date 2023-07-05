n = int(input())
num = list()
for i in range(n):
    num.append(int(input()))

if (num[1] - num[0]) == (num[2]-num[1]):
    print(num[-1] + (num[1] - num[0]))
else:
    print(int(num[-1] * (num[1] / num[0])))
