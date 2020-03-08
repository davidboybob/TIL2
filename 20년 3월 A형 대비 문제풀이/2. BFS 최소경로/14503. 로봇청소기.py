import sys
from pprint import pprint

sys.stdin = open('input_14503.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 북 동 남 서 0 1 2 3
# 0 3 2 1
def rotation(d):
    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    elif d == 2:
        d = 1
    else:
        d = 2
    return d

def searching(d):
    #바라보는 방향의 왼쪽
    if d == 0:
        dx, dy = 0, -1
    elif d == 1:
        dx, dy = -1, 0
    elif d == 2:
        dx, dy = 0, 1
    else:
        dx, dy = 1, 0
    return (dx, dy)

def cleaning(x, y, d):

    data = []

    MAP[x][y] = 2


    return


cleaning(r, c, d)