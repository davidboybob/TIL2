import sys
sys.stdin = open('input_2309.txt', 'r')

lst = [int(input()) for _ in range(9)]

#0 1 2 3 4 5 6 7 8 

#1 << 0 = 1
#1 << 1 = 2
#1 << 2 = 4
N = len(lst)

for i in range(1 << N):
    for j in range(N):
        if i & (1 << j):
            print(lst[j], end=' ')
    print()


