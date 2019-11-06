import sys
sys.stdin = open('input_2146.txt', 'r')


def DFS(sx, sy, count):
    visit[sx][sy] = True

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny =


N = int(input())
island = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*N for _ in range(N)]
count = 1

for x in range(N):
    for y in range(N):
        if island == 1 and visit[x][y] == False:
            count += 1
            DFS(x, y, count)
