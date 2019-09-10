import sys
sys.stdin = open('input_5432.txt', 'r')

TC = int(input())
stack = ''
for tc in range(TC):
    T = input()
    for i in T:
        if i == '(':
            stack += i
        elif i ==')':
            stack += i
            cnt = stack.count('()')
    print(cnt)