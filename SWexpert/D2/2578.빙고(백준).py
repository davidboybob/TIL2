import sys
sys.stdin = open('input_2578.txt', 'r')

B2 = [[0]*5 for _ in range(5)]
count = 0
check = 0
for i in range(5):
    
    B = list(map(int, input().split()))
    B2[i] = B

for a in range(5):
    N = list(map(int, input().split()))
    for k in range(5):
        for i in range(5):
            Sum = 0
            Sum1 = 0
            Sum2 = 0
            Sum3 = 0
            for j in range(5):
                # print(N[k],end=' ')
                # print(B2[i][j], end=' ')
                if B2[i][j] == N[k]:
                    B2[i][j] = 0
                    count += 1
                Sum += B2[j][j]
                Sum1 += B2[j][4-j]
                Sum2 += B2[i][j]
                Sum3 += B2[j][i]
                if Sum==0 and Sum1==0 and Sum2==0 and Sum3==0:
                    check +=1
                if check >= 3:
                    print('bingo')
                    print(count)
                    break
            if check >= 3:
         
               break
        if check >= 3:
         
            break            
    if check >= 3:
        
        break            
            
                
    
