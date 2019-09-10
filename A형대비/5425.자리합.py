import sys
sys.stdin = open('input_5425.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    S, E = map(int, input().split())
    Sum = 0
    for i in range(S, E+1):
        t = i % 10
        n = i // 10
        Sum += t
        while n != 0:
            t = n % 10
            n = n // 10
            Sum += t
    print(Sum)


