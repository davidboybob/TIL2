import sys
sys.stdin = open('input_10815.txt', 'r')

NS = input()
Hand = list(map(int, input().split()))
NC = input()
Q = list(map(int, input().split()))

for i in Q:
    if i in Hand:
        print(1, end=' ')
    else:
        print(0, end=' ')