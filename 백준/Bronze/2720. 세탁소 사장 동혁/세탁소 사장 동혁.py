import sys

n = int(sys.stdin.readline())
money_unit = [0.25, 0.1, 0.05, 0.01]
answer = ''

for i in range(n):
    money = int(sys.stdin.readline()) / 100
    for unit in money_unit:
        for j in range(1, 101):
            if (unit * j) == money:
                answer += str(j) + " "
                money = round(money - (unit * (j)), 2)
                break
            elif (unit * j) >= money:
                answer += str(j - 1) + " "
                money = round(money - (unit * (j - 1)), 2)
                break

    print(answer)
    answer = ''