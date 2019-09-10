import sys
sys.stdin = open('input_1260.txt', 'r')

from collections import deque

# def DFS(S, G):
#     visit = [False] * (V+1)
#     serch = []
#     serch.append(S)
#     visit[S] = True
#     print(S, end=' ')
#
#     while len(serch) > 0:
#         for w in G[S]:
#             if not visit[w]:
#                 serch.append(v)
#                 S = w
#                 visit[w] = True
#                 print(S, end=' ')
#                 break
#         else:
#             S = serch.pop()
#
#
# def BFS(S, G):
#     visit = [False] * (V+1)
#     D = [0] * (V+1)
#
#     Q = deque()
#     Q.append(S)
#     visit[S] = True
#     print(S, end=' ')
#
#     while Q:
#         v = Q.popleft()
#         for w in G[v]:
#             if not visit[w]:
#                 D[w] = D[v] + 1
#                 visit[w] = True
#                 Q.append(w)
#                 print(w, end=' ')
#     print()
#     return D
#
#
# TC = int(input())
# for tc in range(3):
#
#     V, E, S = map(int, input().split())
#     G = [[] for _ in range(V + 1)]
#     for i in range(E):
#         u, v = map(int, input().split())
#         G[u].append(v)
#         G[v].append(u)
#
#     DFS(S, G)
#     print()
#     BFS(S, G)



def DFS(v):
    visit[v] = True
    ans.append(v)

    for w in G[v]:
        if not visit[w]:
            DFS(w)

def BFS(s):
    visit[s] = True
    Q = deque()
    Q.append(s)
    ans.append(s)

    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                Q.append(w)
                ans.append(w)
                visit[w] = True

TC = int(input())
for tc in range(3):

    N, M, s = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    for lst in G:
        lst.sort()

    ans = []
    visit = [False] * (N + 1)
    DFS(s)
    print(' '.join(map(str, ans)))

    ans = []
    visit = [False] * (N + 1)
    BFS(s)
    print(' '.join(map(str, ans)))
