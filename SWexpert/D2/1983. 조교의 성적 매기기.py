import sys
sys.stdin = open('input_1983.txt', 'r')

TC = int(input())

for k in range(TC):
    N, K = map(int, input().split())
    grade = []
    result = [N//10] * 10
    
    for j in range(N):
        lst = list(map(int, input().split()))
        
        Total = (lst[0]*0.35) + (lst[1]*0.45 ) + (lst[2]*0.2)
        grade.append(round(Total))
    
    K = grade[K-1]
    N = N//10
    grade = sorted(grade, reverse=True)
    start = 0

    for i in range(10):
        
        for j in range(i+start, i+start+N):
            if grade[j] == K:
                break
            result[i] -= 1
        start += N-1
        
    for i in range(10):
        if result[i]:
            if i == 0:
                print(f'#{k+1} A+')
                break
            elif i == 1:
                print(f'#{k+1} A0')
                break
            elif i == 2:
                print(f'#{k+1} A-')
                break
            elif i == 3:
                print(f'#{k+1} B+')
                break
            elif i == 4:
                print(f'#{k+1} B0')
                break
            elif i == 5:
                print(f'#{k+1} B-')
                break
            elif i == 6:
                print(f'#{k+1} C+')
                break
            elif i == 7:
                print(f'#{k+1} C0')
                break
            elif i == 8:
                print(f'#{k+1} C-')
                break
            elif i == 9:
                print(f'#{k+1} D0')
                break
