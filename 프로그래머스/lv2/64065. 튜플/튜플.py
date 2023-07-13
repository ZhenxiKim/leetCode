def solution(s):
    data = s[2:-2].split(("},{"))
    answer =[]
    data.sort(key = len)
    for item in data:
        it = item.split(",")
        for i in it:
            if int(i) not in answer:
                answer.append(int(i))
    return answer