import sys
sys.stdin = open('input.txt', 'r')


for k in range(10):
    Sum2 = 0
    Sum3 = 0

    arr = []
    compared = []
    T = int(input())

    for j in range(100):
        Sum = 0

        N = list(map(int, input().split()))
        arr.append(N)
        Sum2 += arr[j][j]
        Sum3 += arr[j][len(arr)-j]

        for i in range(len(arr[j])):
            Sum += arr[j][i]
        compared.append(Sum)

    compared.append(Sum2)
    compared.append(Sum3)
    for j in range(len(arr[0])):
        Sum4 = 0
        for i in range(len(arr)):
            Sum4 += arr[i][j]

        compared.append(Sum4)
    MAX = max(compared)
    print('#{} {}'.format(k+1, MAX))


# for k in range(10):
#     T = int(input())
#     Sum = 0
#     lists = []
#     arr = []
#     for j in range(100):
#
#         N = list(map(int, input().split()))
#         arr.append(N)
#         Sum += arr[j][j]
#     lists.append(Sum)
#     if lists[]
