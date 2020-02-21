N, M = 4, 2


# 1 1
# 1 2
# 2 1

def perm(k):
    if k == M:
        print(*ans)
        return


    for i in range(1, N + 1):
        ans[k] = i
        perm(k + 1)



ans = [0] * M
perm(0)


