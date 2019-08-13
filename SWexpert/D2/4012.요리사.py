import sys
sys.stdin = open('input_4012.txt', 'r')

TC = int(input())

for k in range(1):
    N = int(input())
    synergy = []

    for i in range(N):
        arr = list(map(int, input().split()))
        synergy.append(arr)

    for set in range(1 << N):
        A, B = [], []
        for i in range(N):
            if set & (1 << i):
                A.append(synergy[i])





# arr = [1, 2, 3, 4]
# N = 4
# for set in range(1 << 4):
#     A, B = [], []
#     for i in range(N):
#         if set & (1 << i):
#             A.append(arr[i])
#         else:
#             B.append(arr[i])
#     if len(A) == len(B):
#         print(A, B)