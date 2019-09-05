
import sys
sys.stdin = open('input_2667.txt', 'r')

def DFS(x, y):
    visit[x][y] = True
    ret = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        tx, ty = x + dx, y + dy
        if tx < 0 or tx == N or ty < 0 or ty == N: continue
        if dj[tx][ty] == '0' or visit[tx][ty]: continue
        ret += DFS(tx, ty)
    return ret


N = int(input())
visit = [[False for _ in range(N)] for _ in range(N)]
dj = [input() for _ in range(N)]
cnt = 0
result = []

for j in range(N):
    for i in range(N):
        if dj[j][i] == '1' and not visit[j][i]:
            result.append(DFS(j, i))
            cnt += 1

print(sorted(result))

