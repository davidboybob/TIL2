import sys
sys.stdin = open('sample_input02.txt', 'r')

T = int(input())
lists = [i for i in range(1, 13)]
for k in range(T):
    A = list(map(int, input().split()))
    N, K = A[0], A[1]
    count = 0
    for i in range(1 << 12):
        Sum = 0
        arr = []
        for j in range(12):
            if i & (1 << j):
                Sum += lists[j]
        if Sum == K:
            for j in range(12):
                if i & (1<<j):
                    arr.append(lists[j])
        if len(arr) == N:
            count += 1

    print('#{} {}'.format(k+1, count))
