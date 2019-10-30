import sys
sys.stdin = open('input_2660.txt', 'r')
from collections import deque

def BFS(s):
    global C
    visit = [False] * (N + 1)
    visit[s] = True
    Q = deque()
    Q.append(s)
    f_score = 0

    while Q:
        for _ in range(len(Q)):
            n = Q.popleft()
            for w in G[n]:
                if visit[w] == True: continue
                visit[w] = True
                Q.append(w)
        if Q:
            f_score += 1
    return f_score


N = int(input())
G = [[] for _ in range(N+1)]
C = 1000 #C : chairman
result = []

while True:
    u, v = map(int, input().split())
    if u == -1 or v == -1:
        break
    G[u].append(v)
    G[v].append(u)


for j in range(1, N+1):
    score = BFS(j)
    if score < C:
        if result:
            result = []
        result.append(j)
        C = score
    elif score == C:
        result.append(j)

print(C, len(result))
result.sort()
print(*result)

