def solution(polynomial):
    data = polynomial.split(" + ")
    x = 0
    num = 0
    for c in data:
        if (c[-1]).isalpha():
            if len(c) == 1:
                x += 1
            else:
                x += int(c[:-1])
        else:
            num += int(c)

    if x == 0:
        if num == 0:
            return ''
        return str(num)
    elif x == 1:

        if num>0:
            return "x"+" + "+str(num)
        else:
            return "x"
    else:
        if num == 0: # 3x
            return str(x) + "x"
        else:
            return str(x) + "x" + " + " + str(num)# 3x+7
