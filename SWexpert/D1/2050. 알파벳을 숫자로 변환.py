import sys
sys.stdin = open('input_2050.txt', 'r')

st = str(input())
num = ''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# A ~ Z : 0 ~ 25
for i in st:
    for j in alphabet:
        if i == j:
            i = alphabet.index(j) + 1
            num += str(i) + ' '

print(num)
