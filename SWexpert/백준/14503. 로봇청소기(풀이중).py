'''
출력
1
57
'''


import sys
sys.stdin = open('input_14503.txt', 'r')

from collections import deque
# 시뮬레이션 문제는 문제에 나와있는 그대로 구현하면 됩니다.
N, M = map(int, input().split())

data = list((map(int, input().split())))
MAP = [list(map(int, input().split())) for _ in range(N)]

dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
# dir  0: 북,   1: 동,     2; 남,    3: 서
# left (0, -1)  (-1, 0)   (0, 1),   (1, 0)
# 백트래킹


def DFS(r, c, d, number):
    global cnt
    if number == 4:
        print(cnt)
        return

    for rotation in range(4):
        d += rotation % 4
        dx, dy = dir[d][0], dir[d][1]
        nx, ny = r + dx, c + dy
        d -= 1
        d %= 4
        if not (1 <= nx < N - 1 and 1 <= ny < M - 1): continue
        if MAP[nx][ny] == 0:
            MAP[nx][ny] = 2
            cnt += 1
            DFS(nx, ny, d, 0)
        elif MAP[nx][ny] != 0:
            DFS(r, c, d, number + 1)


    # else:



MAP[data[0]][data[1]] = 2
cnt = 1
DFS(data[0], data[1], data[2], 0)
print(cnt)