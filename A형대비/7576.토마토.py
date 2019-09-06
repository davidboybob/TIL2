import sys
sys.stdin = open('input_7576.txt', 'r')

M, N = map(int, input().split())

Box = [list(map(int, input().split())) for _ in range(N)]

for