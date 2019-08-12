import sys
sys.stdin = open('input_1989.txt', 'r')


TC = int(input())

for k in range(TC):
    T = input()
    for i in range(len(T)//2):
        if T[i] != T[len(T)-1-i]:
            print('#{} 0'.format(k+1))
            break
        else:
            print('#{} 1'.format(k+1))
            break
