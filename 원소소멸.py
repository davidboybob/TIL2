from pprint import pprint
import sys
sys.stdin = open('atom_input.txt', 'r')

def find(i):
    global Q
    for idx in range(len(Q)):
        if i[2] == 0:
            if Q[idx][2] == 1 and Q[idx][1] > i[1] and Q[idx][0] == i[0]:
                result = i[3] + Q[idx][3]

                return result
            elif Q[idx][2] == 2 and abs(Q[idx][0]-Q[idx][1]) == abs(i[0] - i[1]):
                result = i[3] + Q[idx][3]

                return result
            elif Q[idx][2] == 3 and abs(Q[idx][0]-Q[idx][1]) == abs(i[0] - i[1]):
                result = i[3] + Q[idx][3]

                return result
        elif i[2] == 1:
            if Q[idx][2] == 0 and Q[idx][1] < i[1] and Q[idx][0] == i[0]:
                result = i[3] + Q[idx][3]

                return result
            elif Q[idx][2] == 2 and abs(Q[idx][0]-Q[idx][1]) == abs(i[0]- i[1]):
                result = i[3] + Q[idx][3]

                return result
            elif Q[idx][2] == 3 and abs(Q[idx][0]-Q[idx][1]) == abs(i[0]- i[1]):
                result = i[3] + Q[idx][3]

                return result
        elif i[2] == 2:
            if Q[idx][2] == 3 and Q[idx][0] < i[0] and Q[idx][1] == i[1]:
                result = i[3] + Q[idx][3]

                return result
            elif Q[idx][2] == 0 and abs(Q[idx][0]-Q[idx][1]) == abs(i[0]- i[1]):
                result = i[3] + Q[idx][3]

                return result
            elif Q[idx][2] == 1 and abs(Q[idx][0]-Q[idx][1]) == abs(i[0]- i[1]):
                result = i[3] + Q[idx][3]

                return result
        elif i[2] == 3:
            if Q[idx][2] == 2 and Q[idx][0] > i[0] and Q[idx][1] == i[1]:
                result = i[3] + Q[idx][3]

                return result
            elif Q[idx][2] == 0 and abs(Q[idx][0]-Q[idx][1]) == abs(i[0]- i[1]):
                result = i[3] + Q[idx][3]

                return result
            elif Q[idx][2] == 1 and abs(Q[idx][0]-Q[idx][1]) == abs(i[0]- i[1]):
                result = i[3] + Q[idx][3]

                return result

    else:
        return 0


TC = int(input())
for tc in range(1, TC + 1):

    N = int(input())
    #dir = 상(0), 하(1), 좌(2), 우(3)
    arr = [list(map(int, input().split())) for _ in range(N)]
    power = 0
    Q = []

    for i in arr: #i[0]=x, i[1]=y, i[2]=dir, i[3]=P
        if len(Q):
            result = find(i)
            if result:
                power += result
                # print(power)
                # print(Q)
            else:
                Q.append(i)
                # print(Q)
        else:
            Q.append(i)
            # print(Q)
    print(power)