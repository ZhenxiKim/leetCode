import sys

sys.setrecursionlimit(10 ** 6)
MAX = 50 + 10

dicR = [1, -1, 0, 0]
dicC = [0, 0, 1, -1]


def dfs(x, y):
    visited[x][y] = True
    for idx in range(4):
        newX = x + dicR[idx]
        newY = y + dicC[idx]
        if graph[newX][newY] != visited[newX][newY]:
            dfs(newX, newY)


test_case = int(sys.stdin.readline())
for _ in range(test_case):
    # 배추밭 기본 셋팅
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]

    # 배추밭 정보 입력
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x + 1][y + 1] = True

    answer = 0
    for i in range(M + 1):
        for j in range(N + 1):
            if graph[i][j] != visited[i][j]:
                dfs(i, j)
                answer += 1
                
    print(answer)
