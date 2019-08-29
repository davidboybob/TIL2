from pprint import pprint
import sys
sys.stdin = open('input_1979.txt', 'r')

TC = int(input())




for tc in range(1, TC+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    num = 0
    cnt = 0
    cnt2 = 0 
    for j in range(N):
        cnt = 0
        cnt2 = 0    
        for i in range(N):
            if arr[j][i]:
                cnt += 1
            else:
                if cnt == K:   
                    num += 1
                cnt = 0
            if arr[i][j]:
                cnt2 += 1
            else:
                if cnt2 == K:
                    num += 1
                cnt2 = 0
        if cnt == K:   
            num += 1
        if cnt2 == K:
            num += 1
    print('#{} {}'.format(tc,num))


# for k in range(1):
#     N, K = map(int, input().split())
#     arr = []
#     for i in range(N):
#         arr.append(list(map(int, input().split())))
#     cnt = 0
    
#     for j in range(N):
#         Sum = 0
#         for i in range(N):
#             if arr[j][i]:
#                 Sum += arr[j][i]
#             if Sum == K:
#                 cnt += 1

#         print(cnt)