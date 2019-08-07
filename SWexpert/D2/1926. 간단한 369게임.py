
lst = ['3', '6', '9']
es = ''
for i in range(1, 101):
    tmp_lst = []
    tmp_lst += str(i)

    for j in range(len(tmp_lst)):
        if tmp_lst[j] in lst:
            tmp_lst[j] = '-'


            
    es = ''.join(tmp_lst)

    print(es, end= ' ')