import sys

MAX = 50 + 10
sys.setrecursionlimit(10 ** 6)
N, M = map(int, sys.stdin.readline().split())
graph = [['' for _ in range(MAX)] for _ in range(MAX)]
visited = [[False for _ in range(MAX)] for _ in range(MAX)]

for i in range(1, N + 1):
    data = sys.stdin.readline().rstrip()
    for j in range(M):
        graph[i][j + 1] = data[j]


def dfs(y, x):
    visited[y][x] = True
    if graph[y][x] == '-' and graph[y][x + 1] == '-':
        dfs(y, x + 1)

    if graph[y][x] == '|' and graph[y + 1][x] == '|':
        dfs(y + 1, x)


answer = 0

for i in range(N):
    for j in range(M):
        if visited[i + 1][j + 1] == False:
            dfs(i + 1, j + 1)
            answer += 1

print(answer)