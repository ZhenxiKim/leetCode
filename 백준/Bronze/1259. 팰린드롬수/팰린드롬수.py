while True:
    n = str(input())
    if n == '0':
        break
    answer = "yes"
    reverse = n[::-1]

    for i in range(len(n)):
        if n[i] != reverse[i]:
            answer = "no"
    print(answer)
