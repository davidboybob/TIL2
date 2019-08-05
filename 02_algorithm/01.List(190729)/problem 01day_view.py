import sys
sys.stdin = open('input.txt', 'r')

for k in range(1,11):
    N = int(input())
    arr = list(map(int,  input().split()))

    counts = 0

    for j in range(2, len(arr)-2):
        max_list = []
        
        if (arr[j]-arr[j-1])>0 and (arr[j]-arr[j-2])>0 and (arr[j]-arr[j+1])>0 and (arr[j]-arr[j+2])>0:
            for i in range(2, -3, -1):
                if i == 0:
                    continue
                max_list.append(arr[j+i]) 
        
            MAX = max_list[0]
            for x in range(1, 4):
                if max_list[x] > MAX:
                    MAX = max_list[x]
        
            counts += arr[j] - MAX

    print('#{} {}'.format(k, counts))
