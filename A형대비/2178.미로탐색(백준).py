from collections import deque

import sys
sys.stdin = open('input_2178.txt', 'r')

def BFS(sx, sy, ex, ey):

    D = [[0] * M for _ in range(N)]
    D[0][0] = 1
    Q = deque()
    Q.append([sx, sy])


    while Q:
        x, y = Q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            tx, ty = x + dx, y + dy
            if tx < 0 or tx == N or ty < 0 or ty == M: continue
            if arr[tx][ty] == '0' or D[tx][ty]: continue
            D[tx][ty] = D[x][y] + 1
            Q.append([tx, ty])
    return D[ex][ey]

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print(BFS(0, 0, N-1, M-1))
