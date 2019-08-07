# txt = 'The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.'

# txt = str(input())
# print(txt.upper())

# N = int(input())

# for i in range(N):
#     print('#', end = '')


# N= int(input())

# for i in range(N, -1, -1):
#     print(i, end = ' ')
# N = int(input())
# for i in range(N):
#     print(1<<i)


# for i in range(5):
    
#     print('+' * 5)

# N = [3, 2]  
#     #A  B
# #1 : 가위 2: 바위 3: 보 
# N = list(map(int, input().split()))

# if abs(N[0] - N[1]) == 1:
#     if N[0] > N[1]:
#         print('A')
#     else: 
#         print('B')
# else:
#     if N[0] < N[1]:
#         print('A')
#     else:
#         print('B')

# N = int(input())
# num = 1

# while num < N:
#     if N % num == 0:
#         print(f'{num}', end = ' ')
#     num += 1
# print(N, end = '')

# N = list(map(int, input().split()))

# result = N[0] - N[1] + 1
# print(f'{result}')

# N = list(map(int, input().split()))
# a = N[0]
# b = N[1]

# plus = a + b
# Sub = a - b
# mul = a * b
# div = a // b

# print(f'{plus}')
# print(f'{Sub}')
# print(f'{mul}')
# print(f'{div}')

N = int(input())
Sum = 0

for i in range(1, N+1):
    Sum += i
print(Sum)