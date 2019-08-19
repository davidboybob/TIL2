import sys
sys.stdin = open('input_2005.txt', 'r')

TC = int(input())

for tc in range(TC):
    N = int(input())
    print(f'#{TC}')
    print(f'1')
    print(f'1 1')
    for i in range(2, N+1):
        
        