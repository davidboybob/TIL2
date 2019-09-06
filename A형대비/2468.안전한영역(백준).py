from pprint import pprint
from collections import deque

import sys
sys.stdin = open('input_2468.txt', 'r')

def BFS(x, y, H):
    Q.append((x, y))
    flooded_area[x][y] = H
    while len(Q) > 0:
        x, y = Q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            tx, ty = x + dx, y + dy
            if tx < 0 or tx == N or ty < 0 or ty == N: continue
            if area[tx][ty] <= H or flooded_area[tx][ty] == H: continue
            flooded_area[tx][ty] = H
            Q.append((tx, ty))


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

flooded_area = [[0] * N for _ in range(N)]
Max, Min = 0, 1000
for x in range(N):
    for y in range(N):
        if area[x][y] > Max:
            Max = area[x][y]
        if area[x][y] < Min:
            Min = area[x][y]

Q = deque()
ans = 1
for H in range(Min, Max):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] <= H or flooded_area[i][j] == H: continue
            cnt += 1
            BFS(i, j, H)
    ans = max(ans, cnt)
print(ans)

