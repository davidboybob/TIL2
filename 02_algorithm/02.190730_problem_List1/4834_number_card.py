import sys
sys.stdin = open('sample_input_03.txt', 'r')

'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.




[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )

다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )



[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

'''

T = int(input())

for k in range(T):
    N = int(input())
    ai = list(map(int, input()))
    cnt_lst = [0] * 10

    for i in range(N):
        cnt_lst[ai[i]] += 1

    MAX_idx = 0
    MAX_val = cnt_lst[0]
    for j in range(1, 10):
        if MAX_val <= cnt_lst[j]:
            MAX_idx = j
            MAX_val = cnt_lst[j]

    print('#{} {} {}'.format(k+1, MAX_idx, MAX_val))

 # for j in ai:
    #     counts.append(ai.count(j))
    #     # counts 비교 리스트 생성
    # MAX_idx = counts[0]
    # MAX_val = int(ai[0])
    #
    # for i, v in enumerate(counts):
    #
    #     if MAX_idx < v:
    #         if MAX_val < int(ai[i]):
    #             MAX_idx = v
    #             MAX_val = ai[i]
    # print(MAX_val, v)
    #
    # for j in range(N):
    #     for i in ai:
    #         counts.append(ai.count(i))
    #     MAX_idx = counts[0]
    #     MAX_val = int(ai[0])
    #
    #     print(MAX_idx,MAX_val)
