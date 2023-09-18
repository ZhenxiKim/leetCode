import sys

sys.setrecursionlimit(10 ** 6)
N = int(sys.stdin.readline())
MAX = 100000 + 10
graph = [[] for _ in range(MAX)]
visited = [False for _ in range(MAX)]
answer = [0 for _ in range(MAX)]

for _ in range(N-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(idx):
    visited[idx] = True
    for i in range(len(graph[idx])):
        next_idx = graph[idx][i]
        if not visited[next_idx]:
            answer[next_idx] = idx
            dfs(next_idx)


dfs(1)
for j in range(2,N+1):
    print(answer[j])