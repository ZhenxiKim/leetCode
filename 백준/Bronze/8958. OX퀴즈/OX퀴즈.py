n = int(input())

for i in range(n):
    data = list(str(input()))
    answer = 0
    cnt = 0
    for j in data:
        if j == "O":
            cnt +=1
            answer = answer + cnt
        else:
            cnt =0
    print(answer)