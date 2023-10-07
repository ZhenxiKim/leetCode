from collections import deque


def solution(maps):
    answer = 0
    width, height = len(maps[0]),len(maps)
    q= deque()
    visited = [[0 for _ in range(width)] for _ in range(height)]
    q.append((0,0))
    next_path = [(1,0),(-1,0),(0,1),(0,-1)]
    visited[0][0] = 1


    while q:

        x,y = q.popleft()

        for el in next_path:
            nx = x + el[0]
            ny = y + el[1]
            if nx >=0 and ny >= 0 and nx<width and ny <height:
                if maps[ny][nx] and visited[ny][nx] == 0:
                    q.append((nx,ny))
                    visited[ny][nx] = visited[y][x] + 1
    return visited[height-1][width-1] or -1
