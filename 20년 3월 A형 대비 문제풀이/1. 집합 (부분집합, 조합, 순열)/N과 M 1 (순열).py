N, M = 4, 4
ans = [0] * (M)
visit = [False] * (N + 1)

def comb(k):
    if k == M:
        print(ans)
        return

    for i in range(1, N + 1):
        if visit[i]: continue
        visit[i] = True
        ans[k] = i
        comb(k + 1)
        visit[i] = False



comb(0)



