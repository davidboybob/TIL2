import sys
sys.stdin = open('input_2007.txt', 'r')

TC = int(input())

for k in range(TC):
    T = input()
    n = 1

    for i in range(10):
        if T[i:i+n] == T[i+n:i+n+n]:
            print('#{} {}'.format(k+1, n))
            break
        elif T[i:i+n] != T[i+n:i+n+n]:
            n += 1