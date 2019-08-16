TC = int(input())

for k in range(TC):
    N = int(input())
    Sum = 0
    for i in range(1, N+1):
        if i % 2:
            Sum += i
        else:
            Sum -= i

    print(f'#{k+1} {Sum}')