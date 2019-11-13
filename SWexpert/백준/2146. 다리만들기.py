import sys
sys.stdin = open('input_2146.txt', 'r')


from collections import deque


def BFS(z):
    global ans
    D = [[-1]*N for _ in range(N)]
    Q = deque()
    for i in range(N):
        for j in range(N):
            if island[i][j] == z:
                Q.append((i, j))
                D[i][j] = 0
    while Q:
        x, y = Q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue

            if island[nx][ny] and island[nx][ny] != z:
                ans = min(ans, D[x][y])

                return
            if island[nx][ny] == 0 and D[nx][ny] == -1:
                D[nx][ny] = D[x][y] + 1
                Q.append((nx, ny))



def DFS(sx, sy):
    visit[sx][sy] = True
    island[sx][sy] = count
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = sx + dx, sy + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if visit[nx][ny] == True or island[nx][ny] == 0: continue
        visit[nx][ny] = True
        DFS(nx, ny)


N = int(input())
island = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*N for _ in range(N)]
count = 1

ans = 0xfffff


for x in range(N):
    for y in range(N):
        if island[x][y] == 1 and visit[x][y] == False:
            DFS(x, y)
            count += 1


for i in range(1, count+1):
    BFS(i)
print(ans)