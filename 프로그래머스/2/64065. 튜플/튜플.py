import re


def solution(s):
    answer = []

    s = re.sub("^\{","",s)
    s = re.sub("\}$","",s)
    list_a = s.split("},")
    list_a.sort(key=len)

    for data in list_a:
        data = re.sub("[\{\}]","",data)
        list_b = data.split(",")
        for num in list_b:
            c = int(num)
            if c not in answer:
                answer.append(c)


    return answer