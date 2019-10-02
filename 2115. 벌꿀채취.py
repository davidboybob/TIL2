import sys
sys.stdin = open('input_2115.txt', 'r')

# 3<=N<=10, 1<=M<=5, 10<=C<=30, 1<=꿀양<=9


# 1. 가로 M개의 묶음 2개가 채취하는 경우의 수 구하기
# 2. C를 넘지 않는 선에서 최대의 수 빼주면서 벌꿀 가치 구하기
# 3. 최대 값을 비교하여 클때마다 담아가기.

# def work(x, y):
#
#     S = []
#     for i in range(M):
#         visit[x][y+i] = True
#         S.append((x, y+i))
#
#     while len(S):
#
#         # if not visit[x][y]:
'''
def work(x, y):

    for i in range(M):
        if y+M > N: continue
        visit[x][y+i] = True
        data.append(Honey[x][y+i])


    if len(data):
        print(data, visit)
        while x < N:
            for nx in range(x, N):
                if y+M >= N: continue
                for ny in range(N-M+1):
                    if not visit[nx][ny]:
                        for j in range(M):
                            visit[nx][ny+j] = True
                            data.append(Honey[nx][ny+j])

                            visit[nx][ny+j] = False
                        print(data, visit)
                        data.pop()
                        data.pop()

                x += 1

TC = int(input())
for tc in range(1):
    N, M, C = map(int, input().split())

    Honey = [list(map(int, input().split())) for _ in range(N)]


    for i in range(N):


        for j in range(N):
            data = list()
            
            x, y = i, j
            work(x, y)
'''
# 경우의 수 따지기 ( 완전탐색 DFS + 백트래킹)
'''
def DFS(a, b, result, k, c1, c2):
    global Max
    if k == M:
        if c1 >= 0 and c2 >= 0:
            if Max < result:
                Max = result
        return


    DFS(a, b, result + a[k]**2 + b[k]**2, k + 1, c1 - a[k], c2 - b[k])
    DFS(a, b, result + a[k] ** 2, k + 1, c1 - a[k], c2)
    DFS(a, b, result + b[k] ** 2, k + 1, c1, c2 - b[k])
    DFS(a, b, result, k + 1, c1, c2)


TC = int(input())
for tc in range(1, TC+1):
    N, M, C = map(int, input().split())

    Honey = [list(map(int, input().split())) for _ in range(N)]
    Max = 0

    #N*N 을 M의 가로로 나누면, 모든 경우의 수는?
    #4  2 => 3가지 * 4 12C2 => n = (N-M+1) * N, r = 2

    Case = []
    # 모든 경우의 수 구하기.
    for i in range(N):
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(Honey[i][j+k])
            Case.append(tmp)

    # 조합 찾기 => 겹치지 않는 조합 탐색(조건 걸기)
    for p in range(len(Case)):
        visit = [False] * len(Case)

        for l in range(M):
            if p+l > len(Case): continue
            if (p+l)%(N-M+1) == 0: continue
            visit[p+l] = True

        for q in range(p+1, len(Case)):
            if visit[q]: continue
            # print(Case[p], Case[q])
            c1 = c2 = C

    # 최대 상품 가치 일 경우 찾기, 최고의 가치를 찾는 방법: 큰수부터 빼자 경우의 수 따지기 .

            DFS(Case[p], Case[q], 0, 0, c1, c2)


    print('#{} {}'.format(tc, Max))

'''
def comb(k, c, result):
    if k >= M:
        if c >= 0:
            work.append(result)
        return
    else:
        comb(k + 1, c, result)
        comb(k + 1, c - tmp[k], result + tmp[k]**2)



TC = int(input())
for tc in range(1, TC+1):
    N, M, C = map(int, input().split())

    Honey = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False]*N for _ in range(N)]
    Max = 0
    ans = []

    for x in range(N):
        for y in range(N-M+1):
            tmp = []
            for ny in range(y, y+M):
                visit[x][ny] = True
                tmp.append(Honey[x][ny])
            work = []
            comb(0, C, 0)
            Max1 = max(work)

            for p in range(N):
                for q in range(N-M+1):
                    tmp = []
                    for nq in range(q, q+M):
                        if visit[p][nq] == True:
                            break
                        tmp.append(Honey[p][nq])

                    if len(tmp) == M:
                        work = []
                        comb(0, C, 0)
                        Max2 = max(work)
                        if (Max1 + Max2) not in ans:
                            ans.append(Max1 + Max2)
            for ny in range(y, y+M):
                visit[x][ny] = False
    print('#{} {}'.format(tc, max(ans)))
#
#
# def comb(k, n, s):
#     if k >= M:
#         if n <= C:
#             cal_test.append(s)
#         return
#
#     else:
#         comb(k + 1, n, s)
#         comb(k + 1, n + test[k], s + test[k] ** 2)
#
#
# T = int(input())
# for t in range(T):
#     N, M, C = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     select = [[False] * N for _ in range(N)]
#
#     profits = set()
#
#     for y in range(N):
#         for x in range(N - M + 1):
#             test = []
#
#             for s_x in range(x, x + M):
#                 select[y][s_x] = True
#                 test.append(arr[y][s_x])
#
#             cal_test = []
#             comb(0, 0, 0)
#             max_test_1 = max(cal_test)
#             # ------------------------
#             for j in range(N):
#                 for i in range(N - M + 1):
#                     test = []
#
#                     for s_i in range(i, i + M):
#                         if select[j][s_i] == True:
#                             break
#
#                         test.append(arr[j][s_i])
#
#                     if len(test) == M:
#                         cal_test = []
#                         comb(0, 0, 0)
#                         max_test_2 = max(cal_test)
#                         profits.add(max_test_1 + max_test_2)
#             # -----------------------------------------
#             for s_x in range(x, x + M):
#                 select[y][s_x] = False
#
#     print('#{} {}'.format(t + 1, max(profits)))