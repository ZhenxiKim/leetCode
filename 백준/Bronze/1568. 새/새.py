n = int(input())
start = 1
cnt = 0

while(n > 0):
    if n < start:
        start = 1
    n -= start
    start += 1
    cnt +=1
print(cnt)