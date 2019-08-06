import sys
sys.stdin = open('input_2071.txt', 'r')

TC = int(input())

for k in range(TC):
    Sum = 0
    lst = list(map(int, input().split()))
    for i in lst:
        Sum += i

    result = round((Sum/len(lst)))
    
    print(f'#{k+1} {result}')