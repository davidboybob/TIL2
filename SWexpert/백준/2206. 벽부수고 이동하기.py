import sys
sys.stdin = open('input_2206.txt', 'r')

from collections import deque

def BFS(x, y, w):
    global ans
    D[0][0][0] = 1
    Q = deque()
    Q.append((x, y, w))
    while Q:
        x, y, w = Q.popleft()
        if x == N - 1 and y == M - 1:
            ans = D[x][y][w]
            break

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx , ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

            if D[nx][ny][w]: continue
            if Maze[nx][ny] == '0':
                D[nx][ny][w] = D[x][y][w] + 1
                Q.append((nx, ny, w))
            elif w == 0:
                D[nx][ny][1] = D[x][y][w] + 1
                Q.append((nx, ny, 1))

    else:
        ans = -1


N, M = map(int, input().split())

Maze = [input() for _ in range(N)]
D = [[[0, 0] for _ in range(M)] for _ in range(N)]
ans = 0
BFS(0, 0, 0)
print(ans)