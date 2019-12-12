'''
출력
1
57
'''


import sys
sys.stdin = open('input_14503.txt', 'r')




N, M =map(int, input().split())

data = list((map(int, input().split())))
MAP = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
# dir  0: 북,   1: 동,     2; 남,    3: 서
# left (0, -1)  (-1, 0)   (0, 1),   (1, 0)
# 백트래킹
cnt = 0
def DFS(r, c, d):
    global cnt
    visit[r][c] = True
    cnt += 1

    for dd in range(4):
        d0 = (d + dd) % 4
        dr, dc = dir[d0]
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
        if MAP[nr][nc]: continue
        if not visit[nr][nc]:
            DFS(nr, nc, )
        else:






DFS(data[0], data[1], data[2])
print(cnt)
