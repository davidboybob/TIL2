import sys
sys.stdin = open('input_2146.txt', 'r')
from pprint import pprint

from collections import deque


def BFS(lst_point):
    
    while lst_point:



def DFS(sx, sy, count):
    visit[sx][sy] = True

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = sx + dx, sy + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if visit[nx][ny] == True or island[nx][ny] == 0: continue
        visit[nx][ny] = True
        island[nx][ny] = count
        lst_point.append((nx, ny))
        DFS(nx, ny, count)


N = int(input())
island = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*N for _ in range(N)]
count = 1
lst_point = deque()


for x in range(N):
    for y in range(N):
        if island[x][y] == 1 and visit[x][y] == False:
            count += 1
            island[x][y] = count
            DFS(x, y, count)

pprint(island)

BFS(lst_point)