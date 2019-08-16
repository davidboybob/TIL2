import sys
sys.stdin = open('sample_input04.txt', 'r')

T = int(input())

for k in range(T):

    N = int(input())
    lists = list(map(int, input().split()))

    lst = []
    for i in range(0, len(lists)-1):
        min = i
        for j in range(i+1, len(lists)):
            if lists[min] > lists[j]:
                min = j
        lists[i], lists[min] = lists[min], lists[i]

    for i in range((len(lists)//2)):
        lst.append(lists[N-i-1])
        lst.append(lists[i])

    result = list(map(str, lst[:10]))
    results = ' '.join(result)
    print('#{} {}'.format(k+1, results))