N, M = 4 , 2

def comb(k , r):
    if k == M:
        print(ans)
        return

    for i in range(r, N + 1):

        ans[k] = i
        comb(k + 1, i)

ans = [0] * M
comb(0, 1)