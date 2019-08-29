import sys
sys.stdin = open('input_5789.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
    N, Q = map(int, input().split()) #N=상자갯수, Q는 횟수(다음열의 갯수)
    
    Box = [0] * (N+1)
    for q in range(1, Q+1):
        L, R = map(int, input().split())
        for p in range(L, R+1):
            Box[p] = q
    result = ' '.join(map(str, Box[1:]))

    print('#{} {}'.format(tc, result))
