# arr = []
# kdy 123
#
# lo, hi = 0, len(arr) =-1
#
# while lo <= hi:
#     mid = (lo + ji) >> 1
#     if arr[mid] == key:
#         return mid
#     if arr[mid] > key:
#         hi = mid - 1
#     else:
#         lo = mid + 1

arr = [64, 25, 10, 22, 11]
N = len(arr)

for i in range(N-1):
    minIdx = i
    for j in range(i+1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(arr)

#[2, n-1]
#[n-2, n-1]
