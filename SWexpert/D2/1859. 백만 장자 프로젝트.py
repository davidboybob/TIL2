import sys
sys.stdin = open('input_1859.txt', 'r')

TC = int(input())
for k in range(3):
    N = int(input())
    lst = list(map(int, input().split()))
    arr = [0] * N
    buy_cnt = 0

    for i in range(N):
        for j in range(N):
            if lst[i] <= lst[j]:
                arr[i] += 1

    print(arr)




