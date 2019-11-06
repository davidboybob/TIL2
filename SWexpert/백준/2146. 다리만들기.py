import sys
sys.stdin = open('input_2146.txt', 'r')


def DFS():


N = int(input())
island = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*N for _ in range(N)]

for x in range(N):
    for y in range(N):

        DFS(x, y)