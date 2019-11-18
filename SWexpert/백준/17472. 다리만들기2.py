'''
from pprint import pprint

import sys
sys.stdin = open('input_17472.txt', 'r')

N, M = map(int, input().split())
island = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
# 1. 섬을 찾는다. (N개) => 해당 좌표 모두 저장.
# 2. 섬들을 연결하는 (가능한) 다리(간선)를 찾는다.
# 3. 모든 섬들을 연결하려면 결합 컴포넌트가 되기 위한 최소의 간선

# 섬 구별 하기 1 ~ X개의 섬
def DFS(sx, sy):
    visit[sx][sy] = True
    Q.append((sx, sy, cnt))
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = sx + dx, sy + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if island[nx][ny] == 0: continue
        if not visit[nx][ny]:
            island[nx][ny] = cnt
            DFS(nx, ny)

# Q에 섬 좌표 저장
Q = []
cnt = 0
for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            if island[i][j] == 1:

                cnt += 1
                island[i][j] = cnt
                DFS(i, j)

# island 섬 마다 번호가 생김.
# Q 완성
# print(Q, cnt)
# pprint(island)


# 다리 연결하기
# 1. 한 방향으로만 생성가능
# 2. 다리 길이는 2이상
# 3. 교차로는 중복가능
# 4. 다리 길이 최솟값


# 방법 1. 각 섬에서 다른 섬으로 갈 수 있는 모든 다리의 수 저장 후, 최소인 값(데이터) 찾기
# Q 이용하기

# 데이터 저장
G = [[100] * (cnt + 1) for _ in range(cnt + 1)]

for x, y, num in Q:
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        d = 0
        while 0 <= nx < N and 0 <= ny < M:
            if island[nx][ny] == num:
                break
            if island[nx][ny]:
                if 1 < d < G[num][island[nx][ny]]:
                    G[num][island[nx][ny]] = G[island[nx][ny]][num] = d
                break
            d += 1
            nx, ny = nx + dx, ny + dy

# pprint(G)

# PRIM
key = [0] + [0xffff] * cnt
pi = [0] * (cnt + 1)
visited = [False] * (cnt + 1)
key[1] = 0

for _ in range(cnt):
    u = MIN = 0xffff
    for i in range(1, cnt + 1):
        if not visited[i] and MIN > key[i]:
            u, MIN = i, key[i]
    if u == 0xffff: break

    visited[u] = True

    for i in range(1, cnt + 1):
        if G[u][i] != 100 and not visited[i] and G[u][i] < key[i]:
            key[i], pi[i] = G[u][i], u
# print(visited)
# print(key)

if visited.count(True) == cnt: print(sum(key))
else: print(-1)

'''
#--------------------- TRY 2 --------------
from pprint import pprint

import sys
sys.stdin = open('input_17472.txt', 'r')

N, M = map(int, input().split())
island = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]


cnt = 0
data = []
def DFS(sx, sy, cnt):
    island[sx][sy] = cnt
    visit[sx][sy] = True
    data.append((sx, sy, cnt))

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = sx + dx, sy + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if island[nx][ny] == 0: continue
        if not visit[nx][ny]:

            DFS(nx, ny, cnt)


for i in range(N):
    for j in range(M):
        if not visit[i][j] and island[i][j] != 0:
            cnt += 1
            DFS(i, j, cnt)

# pprint(island)
# print(data)

G = [[100] * (cnt + 1) for _ in range(cnt + 1)]
# pprint(G)
for sx, sy, num in data:
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = sx + dx, sy + dy
        d = 0
        while 0 <= nx < N and 0 <= ny < M:
            if island[nx][ny] == num: break
            if island[nx][ny]:
                if 1 < d < G[num][island[nx][ny]]:
                    G[num][island[nx][ny]] = G[island[nx][ny]][num] = d
                break
            d += 1
            nx, ny = nx + dx, ny + dy
print(G)
key = [0] + [0xfffff] * cnt
pi = [0] * (cnt + 1)
visited = [False] * (cnt + 1)
key[1] = 0
for _ in range(cnt):
    u = MIN = 0xffff
    # 시작점 설정
    for i in range(1, cnt + 1):
        if not visited[i] and MIN > key[i]:
            u, MIN = i, key[i]

    if u == 0xffff: break # 한개도 다리 건설 못했을 경우

    visited[u] = True

    for i in range(1, cnt + 1):
        if G[u][i] != 100 and not visited[i] and G[u][i] < key[i]:
            key[i], pi[i] = G[u][i], u
print(key)
print(pi)
print(visited)
if visited.count(True) == cnt: print(sum(key))
else: print(-1)
