import sys
sys.stdin = open('input_2146.txt', 'r')

N = int(input())
island = [list(map(int, input().split())) for _ in range(N)]

