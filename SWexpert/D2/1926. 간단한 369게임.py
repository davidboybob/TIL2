N = int(input())

lst = ['3', '6', '9']
es = ''

for i in range(1, N+1):
    tmp_lst = []
    count = 0
    tmp_lst += str(i)

    for j in range(len(tmp_lst)):
        if tmp_lst[j] in lst:
            count += 1
    if count >= 1:
        tmp_lst = '-' * count
     
    es = ''.join(tmp_lst)

    print(es, end= ' ')
