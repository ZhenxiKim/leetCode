import sys

sys.setrecursionlimit(10 ** 6)
MAX = 100000 + 10
N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(MAX)]
visited = [False for _ in range(MAX)]

global answer
answer = [0 for _ in range(N)]
global order
order = 1

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N + 1):
    graph[i].sort()


def dfs(idx):
    visited[idx] = True
    global order
    answer[idx-1] = order
    order += 1

    data = graph[idx]
    for j in range(len(data)):
        new_idx = data[j]
        if not visited[new_idx]:
            dfs(new_idx)


dfs(R)

for k in answer:
    print(k)
