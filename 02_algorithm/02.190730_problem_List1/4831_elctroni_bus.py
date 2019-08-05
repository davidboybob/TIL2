import sys
sys.stdin = open('sample_input_02.txt', 'r')

'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
 


[예시]



다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.

 

[입력]
 

첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )


각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
 

[출력]


#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.
'''


# 한번충전으로 이동가능 수 K, 정류장 종점 N, 충전기 갯수 M
# 설치된 충전기 위치 list

# 0에서 출발 -> for j in range(11) 0~10 까지 돌리기 종점 N+1
# 최소 이동 수 count -= 1 이동 후 충전소 있으면 count = K, 없으면 count = 0 break: 함수가능?
# 충전소 위치 정해주기 => index 쓰면?? if j ==
# 충전소가 있어도 필요 없다면 지나치고, 도달하지 못한다면, 그전에 충전소가 있었는지 확인해서 다시 충전하기.

# 연료 함수 // 스텝함수 // 남아있는 연료와 남은 거리 비교

# T = int(input())
#
# # for k in range(T):
# lists = list(map(int, input().split()))
# K, N, M = lists[0], lists[1], lists[2] #type int
# M_spot = list(map(int, input().split()))
# fuel = K
# fuel_station = [0] * (N+1)
#
# # for i in range(M):
# #     fuel_station[M_spot[i]] += 1
#
# # print(fuel_station)
# #
# # for j in range(1, K+1):
# #     if fuel > 0:
# #         fuel -= 1  #연료 소비
# #     print(fuel)
#
# # for idx in range(N):
# #     for point in M_spot:
# #         for step in range(idx+1, point+1):
# #             if idx+1 == point:
# #                 fuel = K
# #             if fuel:
# #                 fuel -= 1
# #
# #             print(step, idx, point)
# #             print(fuel)
#
# for i in range()

T = int(input())

for k in range(T):
    lists = list(map(int, input().split()))
    K, N, M = lists[0], lists[1], lists[2] #type int
    M_spot = list(map(int, input().split()))

    fuel_station = [0] * (N+1)



    for i in range(M):
        fuel_station[M_spot[i]] += 1

    start = 0
    step_end = k


    # while True:
        fuel_zero = 0
        for i in range(start+1, step_end+1):
            if fuel_station:
                start = i
            else:
                fuel_zero += 1


T = int(input())

for k in range(T):
    lists = list(map(int, input().split()))
    K, N, M = lists[0], lists[1], lists[2] #type int
    M_spot = list(map(int, input().split()))

    fuel_station = [0] * (N + 1)

    count = 0
    now = 0
    for i in arr:
        station[i] = 1

    while True:
        for i in range(K+now, now, -1):
            if station[i]:
                count += 1
                now = i
                break
            else:
                count = 0
                break
            if now+K >= N:
                break
            print('#{} {}'.format(test_case, count))



