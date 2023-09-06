import sys
sys.setrecursionlimit(10 ** 6)
N = int(sys.stdin.readline())
MAX = 3 + 10 + 100
dx = [1, 0]
dy = [0, 1]
graph = [[0] * MAX for _ in range(MAX)]
visited = [[0] * MAX for _ in range(MAX)]

for i in range(1,N+1):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(len(data)):
        graph[i][j+1] = data[j]

global answer
answer = False


def dfs(x, y):
    if graph[x][y] == -1:
        global answer
        answer = True
        return

    visited[x][y] = 1
    for k in range(2):
        new_x = x + dx[k] * graph[x][y]
        new_y = y + dy[k] * graph[x][y]
        if visited[new_x][new_y] == 0:
            dfs(new_x, new_y)



dfs(1, 1)

if answer:
    print('HaruHaru')
else:
    print('Hing')
