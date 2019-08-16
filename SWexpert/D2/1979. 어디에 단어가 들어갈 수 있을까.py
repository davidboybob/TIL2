import sys
sys.stdin = open('input_1979.txt', 'r')

TC = int(input())

for k in range(1):
    N, K = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    cnt = 0
    
    for j in range(N):
        Sum = 0
        for i in range(N):
            if arr[j][i]:
                Sum += arr[j][i]
            if Sum == K:
                cnt += 1

        print(cnt)

