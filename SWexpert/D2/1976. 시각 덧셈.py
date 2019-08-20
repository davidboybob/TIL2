import sys
sys.stdin = open( 'input_1976(2).txt', 'r')

TC = int(input())
for tc in range(TC):
    lst = list(map(int, input().split()))
    m = 0
    h = 0
    for j in range(len(lst)):
        if j%2:
            m += lst[j]
        else:
            h += lst[j]

    h += m // 60
    m = m % 60
    if h % 12 == 0:
        h = 12
    else:
        h = h % 12
        
    print(f'#{tc+1} {h} {m}')
    

