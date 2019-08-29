from pprint import pprint
import sys
sys.stdin = open('input_5356.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
    arr = [[False] * 15 for _ in range(5)]
    for j in range(5):
        T = input()
        
        for i in range(len(T)):
            arr[j][i] = T[i]

    
    S = ''
    for j in range(15):
        for i in range(5):
            if arr[i][j]:
                S += arr[i][j]
    print('#{} {}'.format(tc, S))
