import sys
sys.stdin = open('input_island.txt', 'r')

def DFS(x, y):
    visit[x][y] = True

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
        tx, ty = x + dx, y + dy
        if tx < 0 or tx == N or ty < 0 or ty == N: continue
        if visit[tx][ty] or island[tx][ty] == 0: continue
        DFS(tx, ty)

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    island = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0

    for x in range(N):
        for y in range(N):
            if island[x][y] and not visit[x][y]:
                DFS(x, y)
                cnt += 1
    print('#{} {}'.format(tc, cnt))


