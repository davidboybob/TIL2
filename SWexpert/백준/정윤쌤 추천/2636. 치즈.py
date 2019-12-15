import sys
sys.stdin = open('input_2636.txt', 'r')
from pprint import pprint
from collections import deque

N, M = map(int, input().split())

Map = [list(map(int, input().split())) for _ in range(N)]


def find_air():

    Q = deque()
    Q.append((0, 0))
    Map[0][0] = 2 # 겉 공기 = 2로 설정

    while Q:
        x, y = Q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if Map[nx][ny] == 0:
                Map[nx][ny] = 2
                Q.append((nx, ny))


def find_cheese(sx, sy):
    q = deque()
    q.append((sx, sy))
    Map[sx][sy] = 3 # 녹을 치즈 3으로 설정.

    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if Map[nx][ny] == 1:
                Map[nx][ny] = 4 # 녹지 않는 치즈 4로 설정.
                if Map[nx + 1][ny] == 2 or Map[nx][ny + 1] == 2 or Map[nx - 1][ny] == 2 or Map[nx][ny - 1] == 2:
                    Map[nx][ny] = 3
                q.append((nx, ny))


def melting():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 2:
                Map[i][j] = 0
            elif Map[i][j] == 3:
                Map[i][j] = 0
                cnt += 1
            elif Map[i][j] == 4:
                Map[i][j] = 1

    return cnt

h = 0

while True:
    h += 1
    find_air()
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 1:
                find_cheese(i, j)
    pre_done = melting()
    if not sum(sum(Map, [])): break

# pprint(Map)
print(h)
print(pre_done)

