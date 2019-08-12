import sys
sys.stdin = open('input_2578.txt', 'r')

B2 = [[0]*5 for _ in range(5)]
count = 0
bingo = 0
N2 = [[0]*5 for _ in range(5)]

for i in range(5):
    
    B = list(map(int, input().split()))
    B2[i] = B

for a in range(5):
    N = list(map(int, input().split()))

    for k in range(5):
        for j in range(5):
            for i in range(5):

                if B2[j][i] == N[k]:
                    N2[j][i] += 1
                    count += 1

                for x in range(5):
                    Sum = 0
                    Sum2 = 0
                    Sum3 = 0
                    Sum4 = 0
                    for y in range(5):
                        Sum += N2[x][y]
                        Sum2 += N2[y][x]
                        Sum3 += N2[y][y]
                        Sum4 += N2[y][4-y]
                        if Sum == Sum2==Sum3==5 or Sum==Sum2==Sum4==5 or Sum==Sum3==Sum4==5 or Sum2==Sum3==Sum4==5:
                            bingo += 1

                        if bingo >= 3:
                            break
                        print(count)
                    if bingo >= 3:
                        break
                if bingo >= 3:
                    break
            if bingo >= 3:
                break
        if bingo >= 3:
            break
    if bingo >= 3:
        break
