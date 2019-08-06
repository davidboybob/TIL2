import sys
sys.stdin = open('sample_input01.txt', 'r')

T = int(input())

for k in range(T):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())
    count = 0
    for a in range(N):
        lists = list(map(int, input().split()))
        r1, c1, r2, c2, color = lists

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if arr[i][j] != color:
                    arr[i][j] += color
                if arr[i][j] == 3:
                    count += 1

    print('#{} {}'.format(k + 1, count))
