import sys
sys.stdin = open('input_2001.txt', 'r')

TC = int(input())

for k in range(TC):
    N, M = map(int, input().split())
    lst = []
    for j in range(N):
        T = list(map(int, input().split()))
        lst.append(T)
    Sum = 0
    for j in range(N-M+1):
        for start in range(N-M+1):
            fly_num = 0
            for i in range(M):
                fly_num += lst[j][start + i]
                for second in range(1, M):
                    fly_num += lst[j+second][start + i]
                if Sum < fly_num:
                    Sum = fly_num
    print(f'#{k+1} {Sum}')