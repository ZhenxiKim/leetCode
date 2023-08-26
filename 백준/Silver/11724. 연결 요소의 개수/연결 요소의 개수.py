import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().split())
MAX = 1000 + 10
graph = [[False for _ in range(MAX)] for _ in range(MAX)]
visited = [False for _ in range(MAX)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = True
    graph[y][x] = True


def dfs(idx):
    visited[idx] = True
    for j in range(1, N + 1):
        if not visited[j] and graph[idx][j]:
            dfs(j)


cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
