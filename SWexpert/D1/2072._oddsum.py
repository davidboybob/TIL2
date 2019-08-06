import sys
sys.stdin = open('input_2072.txt', 'r')

TC = int(input())

for k in range(1, TC+1):
    N = list(map(int, input().split()))
    Sum = 0
    for i in N:
        if i & 1:
            Sum += i
    print(f'#{k} {Sum}')
