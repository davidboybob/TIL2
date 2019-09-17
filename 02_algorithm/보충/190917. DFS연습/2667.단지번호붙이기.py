import sys
sys.stdin = open('input_2667.txt', 'r')

def solving(sx, sy):
    global lst, cnt

    visit[sx][sy] = True

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        tx, ty = sx + dx, sy + dy
        if tx < 0 or tx == N or ty < 0 or ty == N: continue
        if not visit[tx][ty] or danji[tx][ty] == 0: continue
        cnt += 1

        solving(tx, ty)



N = int(input())
danji = [input() for _ in range(N)]
visit = [[False] * N for _ in range(N)]
lst = []
cnt = 0

for x in range(N):
    for y in range(N):
        if danji[x][y] == '1' and not visit[x][y]:
            solving(x, y)

