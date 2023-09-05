import sys

sys.setrecursionlimit(10 ** 6)
MAX = 60
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]


def dfs(x, y):
    visited[x][y] = True

    for k in range(8):
        nex_x = x + dx[k]
        new_y = y + dy[k]
        if visited[nex_x][new_y] == False and graph[nex_x][new_y]:
            dfs(nex_x, new_y)


while True:
    col, row = map(int, sys.stdin.readline().split()) # 열, 행
    if col == 0 and row == 0:
        break

    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]

    # graph 셋팅
    for i in range(1, row + 1):
        data = list(sys.stdin.readline().split())
        for j in range(1, len(data) + 1):
            if data[j - 1] == '1':
                graph[i][j] = True
            else:
                graph[i][j] = False

    answer = 0
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if graph[i][j] and visited[i][j] == False:
                dfs(i, j)
                answer += 1

    print(answer)
