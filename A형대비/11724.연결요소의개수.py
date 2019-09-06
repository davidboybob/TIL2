import sys
sys.stdin = open('input_11724.txt', 'r')


def DFS(s):
    visit[s] = 1
    for w in G[s]:

        if visit[w] == 0:
            DFS(w)


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    visit = [0] * (N + 1)
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)


    cnt = 0
    for i in range(1, N+1):
        if visit[i] == 0:
            DFS(i)
            cnt += 1
    print(cnt)
