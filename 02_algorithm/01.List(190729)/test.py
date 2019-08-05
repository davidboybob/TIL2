import sys
sys.stdin = open('input_test.txt', 'r')

# N = int(input())
#
# arr = []
# for i in range(N):
#     arr.append(int(input()))

N = int(input())
arr = list(map(int,  input().split()))

# print(N, arr)
# 2번 기준부터 시작  n-2 까지 돌리기 --> for i in range(2, len(arr)-2)
# 기준으로 부터 n-1,n-2 와 n+1, n+2 (양쪽 건물이) 있냐 없냐 판별 (해당 리스트와의 차가 0이상)-->
#
# 
counts = 0

for j in range(2, len(arr)-2):
    max_list = []
    
    if (arr[j]-arr[j-1])>0 and (arr[j]-arr[j-2])>0 and (arr[j]-arr[j+1])>0 and (arr[j]-arr[j+2])>0:
        for i in range(2, -3, -1):
            if i == 0:
                continue
            max_list.append(arr[j+i]) 
        # print(max_list)
        MAX = max_list[0]
        for x in range(1, 4):
                if max_list[x] > MAX:
                        MAX = max_list[x]
        # print(MAX)
        counts += arr[j] - MAX

# 전망 좋은 층의 갯수 구하기. 밑에서 부터 제외하기 // 큰 숫자 비교하기






print (arr[j])
print(counts)
