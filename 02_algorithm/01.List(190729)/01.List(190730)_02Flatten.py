import sys
sys.stdin = open('test02.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))

# for dump in range(N):
count = 0

for dump in range(N):
    for idx in range(10): # 가로길이 100

        if arr[idx] == max(arr):
            arr[idx] -= 1
            count += 1

            for idx2 in range(10):
                if arr[idx2] == min(arr):
                    arr[idx2] += 1


print(count)
print(arr)
print(max(arr))
print(min(arr))


#     for
#         MIN += 1
#         MAX -= 1
#
# arr[idx] = MAX
# arr[idx] = MIN