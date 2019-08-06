import sys
sys.stdin = open('input_2068.txt', 'r')

TC = int(input())

for k in range(1, TC+1):
    lst = list(map(int, input().split()))
    Max = 0

    for i in range(len(lst)):
        if Max < lst[i]:
            Max = lst[i]
    
    print(f'#{k} {Max}')