import sys
sys.stdin = open('input_1210.txt', 'r')

def DFS(sx, sy, dir):
    if sy == 0:
        return sx

    ladder[sy][sx] = 0


    if dir == 0:
        for dx, dy in [(-1, 0), (1, 0), (0, -1)]:
            tx, ty = sx + dx, sy + dy
            if tx < 0 or tx == N or ty < 0 or ty == N: continue
            if ladder[ty][tx] == 0: continue
            if dx == -1:
                dir = 1

            elif dx == 1:
                dir = 2

            DFS(tx, ty, dir)

    elif dir == 1:
        for dx, dy in [(-1, 0), (1, 0), (0, -1)]:
            tx, ty = sx + dx, sy + dy
            if tx < 0 or tx == N or ty < 0 or ty == N: continue
            if ladder[ty][tx] == 0: continue
            if dy == -1:
                dir = 0

            DFS(tx, ty, dir)

    else:
        for dx, dy in [(-1, 0), (1, 0), (0, -1)]:
            tx, ty = sx + dx, sy + dy
            if tx < 0 or tx == N or ty < 0 or ty == N: continue
            if ladder[ty][tx] == 0: continue
            if dy == -1:
                dir = 0

            DFS(tx, ty, dir)


for tc in range(10):
    N = int(input()) #케이스
    ladder = [list(map(int, input().split())) for _ in range(100)]

    dir = 0  # 0: 위, 1: 좌, 2: 우
    for i in range(100):
        if ladder[99][i] == 2:
            s = i


    result = DFS(s, 99, dir)


