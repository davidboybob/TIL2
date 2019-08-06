import sys
sys.stdin = open('input_2070.txt', 'r')

TC = int(input())

for k in range(TC):
    lst = list(map(int, input().split()))
    if lst[0] < lst[1]:
        print(f'#{k+1} <')
    elif lst[0] == lst[1]:
        print(f'#{k+1} =')
    else:
        print(f'#{k+1} >')