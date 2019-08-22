import sys
sys.stdin = open ('input_01.txt', 'r')

TC = int(input())

for tc in range(10):
    N = int(input())
    cnt = [0] * 3
    Max = 0
    arr = [list(map(int, input().split())) for _ in range(N)]

    for j in range(N):
        
        for i in range(N):
            Sum_x = 0
            Sum_y = 0
            for y in range(N):
                Sum_x += arr[j][y]
                Sum_y += arr[y][i]
            
            Sum = Sum_x + Sum_y - arr[j][i]
        #     print(Sum_x, Sum_y, Sum)
        # print()
        
            if Sum >= Max:
                
                Max = Sum
                cnt[0] = j
                cnt[1] = i
                cnt[2] = Max
    
    print(f'#{tc+1} {cnt[0]} {cnt[1]} {cnt[2]}')
