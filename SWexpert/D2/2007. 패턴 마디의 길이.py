import sys
sys.stdin = open('input_2007.txt', 'r')

TC = int(input())

for k in range(TC):
    lst = [0] * 10   
    text = input()
    txt_lst = []

    for i in range(10):
        txt_lst += text[i]
    print(txt_lst)
