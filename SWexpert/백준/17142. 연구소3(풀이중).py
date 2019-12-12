#out put
'''
4
4
4
3
7
-1
0
'''
from pprint import pprint
import sys
sys.stdin = open('input_17142.txt', 'r')
#
# # 0 은 빈칸, 1은 벽, 2는 바이러스를 놓을 수 있는 위치. 1<=M < 2의 개수 <= 10
# from collections import deque
# TC = int(input())
# for tc in range(TC):
#     N, M = map(int, input().split())
#     Labor = [list(map(int, input().split())) for _ in range(N)]
#     # pprint(Labor)
#     possible = []
#
#     for i in range(N):
#         for j in range(N):
#             if Labor[i][j] == 2:
#                 possible.append((i, j))
#     # print(possible)
#
#     # 조합 len(possible)Cm
#     combination = [0] * M
#     visit = [False] * len(possible)
#     data = []
#     def comb(k, r):
#         if k == M:
#             data.append(tuple(combination))
#             # print(combination)
#             return
#
#         else:
#             for i in range(r, len(possible)):
#                 if visit[i]: continue
#                 visit[i] = True
#                 combination[k] = i
#                 comb(k + 1, i + 1)
#                 visit[i] = False
#     comb(0, 0)
#     # print(data)
#
#     # 조합별로 바이러스 설치해서 BFS 해서 최대 거리 가 최소인 값을 출력
#     Min = 0xfffff
#     def BFS(p):
#         global Min
#         Ml = -1
#         visit = [[False] * N for _ in range(N)]
#         D = [[0] * N for _ in range(N)]
#         Q = deque()
#         for j in p:
#             Q.append(possible[j])
#
#         while Q:
#             sx, sy = Q.popleft()
#             # visit[sx][sy] = True
#             for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#                 nx, ny = sx + dx, sy + dy
#                 if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
#                 if Labor[nx][ny] == 1:
#                     # visit[nx][ny] = True
#                     continue
#                 if Labor[nx][ny] == 2:
#                     # visit[nx][ny] = True
#                     continue
#                 if not visit[nx][ny]:
#                     visit[nx][ny] = True
#                     D[nx][ny] = D[sx][sy] + 1
#
#                     Ml = max(Ml, D[nx][ny])
#                     Q.append((nx, ny))
#
#         # print(Ml)
#         Min = min(Ml, Min)
#         # print(Min)
#         # pprint(Labor)
#         # pprint(visit)
#         # pprint(D)
#         # pprint(visit)
#         for i in range(N):
#             for j in range(N):
#                 if Labor[i][j] != 1 and Labor[i][j] != 2 and not visit[i][j]:
#                     # pprint(D)
#
#
#     for i in data:
#         BFS(i)
#         # print(possible[j])
#
#     print(Min)



#------ try 2-----------------

from collections import deque

def BFS(new_Labor, data):
    global Min
    visit = [[False] * N for _ in range(N)]
    Q = deque()
    for i in data:
        visit[i[0]][i[1]] = True

        Q.append(i)

    while Q:
        sx, sy = Q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = sx + dx, sy + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if new_Labor[nx][ny] == '*' or new_Labor[nx][ny] == '-': continue
            if not visit[nx][ny] and new_Labor[nx][ny] == 0:
                visit[nx][ny] = True
                new_Labor[nx][ny] = new_Labor[sx][sy] + 1
                Q.append((nx, ny))

    if Min > new_Labor[sx][sy]:
        cnt = 0
        for i in range(N):
            for j in range(N):
                if new_Labor[i][j] == 0:
                    cnt += 1
        # pprint(new_Labor)
        if cnt == M:
            Min = new_Labor[sx][sy]



TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    Labor = [list(map(int, input().split())) for _ in range(N)]
    sel = []

    # 조합 짜기
    for i in range(N):
        for j in range(N):
            if Labor[i][j] == 2:
                sel.append((i, j))
    # pprint(Labor)
    # print(sel)
    data = [0] * M
    Min = 0xfffff

    def comb(k, r):
        if k == M:
            # print(data)
            new_Labor = [[0] * N for _ in range(N)]
            # 새로운 배열 생성
            for ii in range(N):
                for jj in range(N):
                    if Labor[ii][jj] == 2 and (ii, jj) in data:
                        new_Labor[ii][jj] = 0
                    elif Labor[ii][jj] == 2 and (ii, jj) not in data:
                        new_Labor[ii][jj] = '*'
                    elif Labor[ii][jj] == 1:
                        new_Labor[ii][jj] = '-'
            # pprint(new_Labor)
            # print(data)
            BFS(new_Labor, data)

            return

        for i in range(r, len(sel)):
            data[k] = sel[i]
            comb(k + 1, i+1)

    comb(0, 0)
    if Min != 0xfffff:
        print(Min)
    else:
        print(-1)