import sys
sys.stdin = open('input_10163.txt', 'r')

TC = int(input())

arr = [[0] *10 for _ in range(10)]
cnt = [0]*(TC+1)
#좌 하 = (0,0) # 우 상 = (101, 101)
for k in range(1, TC+1):
    zero_x, zero_y, x, y = map(int, input().split())
    
    for j in range(-zero_y-1, -zero_y-1-y, -1): #y축 열
        for i in range(zero_x, zero_x+x): #x축 행 
            arr[j][i] = k

for j in arr:
    for i in j:
        if i:
            cnt[i] += 1
for i in cnt[1:]:
    print(i)