N = int(input())

answer = 0
for i in range(1, N + 1):
    result = i + sum(map(int, str(i)))
    if result == N:
        answer = i
        break

print(answer)
