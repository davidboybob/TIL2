import sys
sys.stdin = open('sample_input03.txt', 'r')

T = int(input())

for k in range(T):
    N = list(map(int, input().split()))
    result = []
    for j in range(2):
        start = 1
        end = N[0]
        page = N[j+1]
        cnt = 0

        while start <= end:
            mid = (start + end) // 2
            if mid == page:
                break
            elif mid > page:
                end = mid
                cnt += 1
            else:
                start = mid
                cnt += 1

        result.append(cnt)

    if result[0] < result[1]:
        print('#{} A'.format(k+1))
    elif result[0] == result[1]:
        print('#{} 0'.format(k+1))
    else:
        print('#{} B'.format(k+1))