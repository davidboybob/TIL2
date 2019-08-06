import sys
sys.stdin = open('input_2056.txt', 'r')

TC = int(input())

for k in range(1, TC+1):
    st = str(input())
    Y = ''
    M = ''
    D = ''
    Sum = ''
    for i in range(4):
        Y += st[i]

    for i in range(4,6):
        M += st[i]
    
    for i in range(6, 8):
        D += st[i]

    if 1<=int(M)<=12:
        
        if int(M)==2 and 1<=int(D)<=28:
            Sum = Y
            Sum += '/' + M
            Sum += '/' + D
            print(Sum)
        elif int(M)==4 and 1<=int(D)<=30:
            Sum = Y
            Sum += '/' + M
            Sum += '/' + D
            print(Sum)
        elif int(M)==6 and 1<=int(D)<=30:
            Sum = Y
            Sum += '/' + M
            Sum += '/' + D
            print(Sum)
        elif int(M)==9 and 1<=int(D)<=30:
            Sum = Y
            Sum += '/' + M
            Sum += '/' + D
            print(Sum)
        elif int(M)==11 and 1<=int(D)<=30:
            Sum = Y
            Sum += '/' + M
            Sum += '/' + D
            print(Sum)
        elif int(M)==1 and 1<=int(D)<=31:
            Sum = Y
            Sum += '/' + M
            Sum += '/' + D
            print(Sum)
        elif int(M)==3 and 1<=int(D)<=31:
            Sum = Y
            Sum += '/' + M
            Sum += '/' + D
            print(Sum)
        elif int(M)==5 and 1<=int(D)<=31:
            Sum = Y
            Sum += '/' + M
            Sum += '/' + D
            print(Sum)
        elif int(M)==7 and 1<=int(D)<=31:
            Sum = Y
            Sum += '/' + M
            Sum += '/' + D
            print(Sum)
        elif int(M)==8 and 1<=int(D)<=31:
            Sum = Y
            Sum += '/' + M
            Sum += '/' + D
            print(Sum)
        elif int(M)==10 and 1<=int(D)<=31:
            Sum = Y
            Sum += '/' + M
            Sum += '/' + D
            print(Sum)
        elif int(M)==12 and 1<=int(D)<=31:
            Sum = Y
            Sum += '/' + M
            Sum += '/' + D
            print(Sum)
        else:
            print(-1)
    else:
        print(-1)