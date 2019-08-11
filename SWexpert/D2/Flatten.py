import sys
sys.stdin = open('input_flatten.txt', 'r')

for k in range(10):
    N = int(input())
    dump_lst = list(map(int, input().split()))
    count = 0
    MAX = 0
    MIN = 0
    
    while count <= N:
        MAX = max(dump_lst)
        MIN = min(dump_lst)

        for i in range(len(dump_lst)):
            if dump_lst[i] == MAX:
                dump_lst[i] -= 1
                
                for j in range(len(dump_lst)):
                    if dump_lst[j] == MIN:
                        dump_lst[j] += 1
                        count += 1
                        break
                break

        
        if (MAX - MIN) <= 1 :
            break
    print(f'#{k+1} {MAX - MIN}')





