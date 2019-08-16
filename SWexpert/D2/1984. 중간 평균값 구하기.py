import sys
sys.stdin = open('input_1984.txt', 'r')

TC = int(input())

for k in range(TC):
    N = list(map(int, input().split()))

    
    # 선택정렬
    for i in range(len(N)-1):
        minidx = i
        for j in range(i+1,len(N)):
            if N[minidx] > N[j]:
                minidx = j
        N[minidx], N[i] = N[i], N[minidx]
    Sum = 0
    for i in range(1, len(N)-1):
        Sum += N[i]
    Sum = Sum / 8

    print(f'#{k+1} {round(Sum)}')
    