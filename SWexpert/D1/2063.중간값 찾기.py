import sys
sys.stdin = open('input_2063.txt', 'r')

N = int(input())

lst = list(map(int, input().split()))
Sum = 0

for i in range(len(lst)-1):
    Min_idx = i
    for j in range(i+1,len(lst)):
        if lst[Min_idx] < lst[j]:
            Min_idx = j
    lst[i], lst[Min_idx] = lst[Min_idx], lst[i]


print(lst[99])