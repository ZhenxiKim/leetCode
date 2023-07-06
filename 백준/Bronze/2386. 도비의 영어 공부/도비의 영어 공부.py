while True:
    data = list(input().split())
    if data[0] == "#":
        break
    sentenct = ''.join(data[1:])
    cnt = 0
    for i in sentenct:
        if str(data[0]).lower() == str(i).lower():
            cnt+=1
    print(data[0] , cnt)
