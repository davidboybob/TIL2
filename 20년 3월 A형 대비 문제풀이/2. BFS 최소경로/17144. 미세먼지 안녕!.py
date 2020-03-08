'''
1 188
2 188
3 186
4 178
5 172
6 71
7 52
8 46

'''
from pprint import pprint
# 1. 미세먼지 확산
import sys
from collections import deque

sys.stdin = open('input_17144.txt', 'r')

R, C, T = map(int, input().split())

dust = [list(map(int, input().split())) for _ in range(R)]

pprint(dust)

# 문제파악 : 1조건 2조건을 해결하는 시뮬레이션 문제
# 방법 : BFS -> 먼지 퍼지는 것, 바람 이동 -> stack,
# 세부 사항 : 미세먼지 확산 시, 4방향 탐색 -> 확산 가능 하면 확산
#            맵 내에서 기존과 새로운 맵을 정리하는 방법이 필요.


def diffusion(data):
    visit = [[False] * C for _ in range(R)]
    Q = deque()
    pprint(visit)

    while Q:
        x, y = Q.popleft()
        if dust[x][y]:

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= R or ny < C or ny >= C: continue


    return

data = []

for i in range(R):
    for j in range(C):
        if dust[i][j] == -1 or dust[i][j] == 0:
            continue

        data.append((i, j))
print(data)
diffusion(data)