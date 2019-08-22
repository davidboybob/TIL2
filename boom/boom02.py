import sys
sys.stdin = open ('input_02.txt', 'r')

TC = int(input())

for tc in range(1):
    N = int(input())
    cnt = [0] * 3
    
    arr = [list(map(int, input().split())) for _ in range(N)]

    for j in range(N):
        arr[j][j]