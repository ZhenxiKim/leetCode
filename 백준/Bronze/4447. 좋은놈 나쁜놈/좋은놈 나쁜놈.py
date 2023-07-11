import sys

n = int(sys.stdin.readline())

for i in range(n):
    result = "NEUTRAL"
    txt = str(input())
    g_cnt = 0
    b_cnt = 0
    for j in txt:
        if j.lower() == "g":
            g_cnt += 1
        elif j.lower() == "b":
            b_cnt += 1

    if g_cnt < b_cnt:
        result = "A BADDY"
    elif g_cnt > b_cnt:
        result = "GOOD"

    print(txt + " is " + result)
