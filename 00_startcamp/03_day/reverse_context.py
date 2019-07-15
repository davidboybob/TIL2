#DOCstring

"""
이 함수는 설명문 (누가만들고 이렇게 사용하시면됩니다. 코멘트 달기 주석과는 차이점 있음.

"""
"""
다음과 같은 내용의 파일 quest.txt가 있다.
0
1
2
3

이 파일의 내용을 다음과 같이 역순으로 reverse_quest.txt라는 파일로 저장하시오.
3
2
1
0
hint) 1. 읽고 2. 뒤집고 3. 작성하고
"""

with open('quest.txt','w') as f: 
     for i in range(4):
         f.write(f'{i}\n')
         print(f'{i}')

with open('quest.txt','r') as f:
    reverse = f.readlines()[::-1] #읽어온 파일의 리스트를 역순으로 하기.
    print(reverse)

with open('reverse_quest.txt','w') as f: #for문으로 입력하기
    for reverse_ in reverse:
        f.write(f'{reverse_}')
        print(f'{reverse_}')


# 1. 읽고
with open('quest.txt', 'r') as f:
    lines = f.readlines()

# 2. 뒤집고
lines.reverse()

# 3. 작성하고
with open('reverse_quest.txt', 'w') as f:
    for line in lines:
        f.write(line)

with open('reverse_quest.txt', 'w') as f:
    f.writelines(lines)

