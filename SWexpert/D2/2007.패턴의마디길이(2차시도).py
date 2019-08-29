import sys
sys.stdin = open('input_2007.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
    T = input()
    s = ''
    bp = 0
    for i in range(10):
        s += T[i]

        for j in range(0, len(T), len(s)):
            
            if s != T[j+len(s):j+len(s)+len(s)]:
                break
            else:
                print('#{} {}'.format(tc, len(s)))
                bp = 1
                break
                
        if bp == 1:
            break
                

