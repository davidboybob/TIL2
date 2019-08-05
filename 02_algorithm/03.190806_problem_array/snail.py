# 5 x 5 배열
arr = [
    [12, 19, 23, 14, 17],
    [21, 20, 25, 9, 11],
    [10, 1, 13, 4, 16],
    [15, 5, 18, 2, 24],
    [6, 22, 3, 7, 8]
]

arr = [[0]*5 for i in range(5)]

count = 1

for j in range(5):

    arr[0][j] = count
    count += 1

for i in range(1, 5):
    arr[i][4] = count
    count += 1

for 

    print(arr)
# for i in range(1, 5):
#     arr[i][4] = arr[i][4] + 1


