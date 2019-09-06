import sys
sys.stdin = open('input_15686.txt', 'r')

TC = int(input())
for tc in range(1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    home = []
    chicken = []
    v = []

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 2:
                DFS(x, y)