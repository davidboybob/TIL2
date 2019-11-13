import sys
sys.stdin = open('input_17471.txt', 'r')

def DFS(v, arr, visit):
    visit[v] = True
    for w in G[v]:
        if w in arr and not visit[w]:
            DFS(w, arr, visit)


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    P = [0] + list(map(int, input().split()))
    Sum_A, Sum_B, Min = 0, 0, 10000
    G = [[] for _ in range(N+1)]
    # print(P)
    for i in range(1, N+1):
        data = list(map(int, input().split()))
        for j in range(1, len(data)):
            G[i].append(data[j])

    # 부분집합으로 두 부분으로 나누기
    A, B = [], []

    def subset(k, A, B):
        if k == N+1:
            global Sum_A, Sum_B, Min
            if A and B:
                visit = [False] * (N + 1)
                DFS(A[0], A, visit)
                if len(A) == visit.count(True):
                    for p in A:
                        Sum_A += P[p]

                visit = [False] * (N + 1)
                DFS(B[0], B, visit)
                if len(B) == visit.count(True):
                    # print(B)
                    for q in B:
                        # print(q)
                        # print(P[q])
                        # print(B)
                        Sum_B += P[q]

                # print(A, B)
                # print(Sum_A, Sum_B)
                if Sum_A != 0 and Sum_B != 0:
                    Min = min(Min, abs(Sum_A - Sum_B))
                Sum_A, Sum_B = 0, 0
                # print(Min)
            return

        subset(k + 1, A + [k], B)
        subset(k + 1, A, B + [k])

    subset(1, A, B)
    if Min == 10000:
        Min = -1
    print(Min)