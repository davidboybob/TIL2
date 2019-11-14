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
print(Q)
pprint(island)


dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# 다리 연결하기
# 1. 한 방향으로만 생성가능
# 2. 다리 길이는 2이상
# 3. 교차로는 중복가능
# 4. 다리 길이 최솟값


# 방법 1. 각 섬에서 다른 섬으로 갈 수 있는 모든 다리의 수 저장 후, 최소인 값(데이터) 찾기
# Q 이용하기
def Bridge(data):
    x, y, num = Q.pop(0):
    while Q:
        q = [(x, y, num)]
        while q:


Bridge(Q)




