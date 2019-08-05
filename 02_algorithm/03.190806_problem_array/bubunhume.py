arr = [3, 6, -2, 7, -3, 1, -5, -1, 5, 4]

N = len(arr)

for i in range(1 << N): #i 는 부분집합을 표현하는 값을 의미
    Sum = 0
    for j in range(N):
        if i & (1 << j): # arr[j]를 포함하는지
            Sum += arr[j]

    if Sum == 0:
        for j in range(N):
            if i & (1<<j):
                print(arr[j], end=' ')
        print()
