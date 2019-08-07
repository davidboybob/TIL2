import sys
sys.stdin = open('input_2007.txt', 'r')

TC = int(input())

for k in range(TC):
    text = input()
    txt = text[0]
    count = 1
    for i in range(1, len(text)):
        count += 1
        