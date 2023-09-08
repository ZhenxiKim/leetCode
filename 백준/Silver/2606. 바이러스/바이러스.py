import sys
sys.setrecursionlimit(10 ** 6)
MAX = 100 + 10
N = int(sys.stdin.readline())  # 컴퓨터의 수
M = int(sys.stdin.readline())  # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
graph = [[False] * MAX for _ in range(MAX)]
visited = [False for _ in range(MAX)]

# graph 셋팅
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = True
    graph[y][x] = True


def dfs(i):
    visited[i] = True
    for j in range(1, N + 1):
        if not visited[j] and graph[i][j]:
            dfs(j)


dfs(1)

print(visited.count(True) - 1)
