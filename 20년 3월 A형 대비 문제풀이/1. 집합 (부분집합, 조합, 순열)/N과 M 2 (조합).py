N, M = 4, 2

def comb(k, r):
    if k == M:
        print(arr)
        return

    for i in range(r, N + 1):
        if not visit[i]:
            visit[i] = True
            arr[k] = i
            comb(k + 1, i + 1)
            visit[i] = False



visit = [False] * (N + 1)
arr = [0] * M

comb(0, 1)