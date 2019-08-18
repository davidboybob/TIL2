import sys
sys.stdin = open('input_1859.txt', 'r')

TC = int(input())

for k in range(TC):
    N = int(input())
    lst = list(map(int, input().split()))
    arr = [0] * N
    
    Sum = 0
    for i in range(N):
        for j in range(i+1, N):
            if lst[i] <= lst[j]:
                arr[i] += 1
                break
    
    for i in range(N):
        if arr[i]:
            for j in range(i+1, N):
                if arr[j] == 0:
                    Sum += lst[j] - lst[i]
                    break
    print(f'#{k+1} {Sum}')


# for k in range(TC):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     cnt = 0
#     Sum = 0

    
        
