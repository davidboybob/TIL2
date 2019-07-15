#변수에 만들고 싶은 파일을 open() 해야 한다.
#open() 할때 r: 읽기 / W: 쓰기(+덮어쓰기) / a: 추가
#f = open('만들 파일 명', '행동')
f = open('ssafy.txt', 'w')

for i in range(10):
    f.write(f'This is line {i+1}.\n')
f.close() #open 은 close로 항상 닫아줘야 한다.
# with 구문 (context manager)

with open('with_ssafy.txt', 'w') as f:
    for i in range(10):
        f.write(f'This is line {i+1}.\n')

#이스케이프 문자
#\n : 개행문자 (다음 줄 이동)
#\t : 탭문자 (tab의 역할)
#\\ : 백슬래쉬 출력
#\' : 작은따옴표 출력
#\" : 큰따옴표 출력
# '문자열'.strip() : 이스케이프문자 삭제함수           rstrip()         lstrip()

#writelines() : list 를 넣어주면, 요소 하나당 한 줄 씩 작성한다.
with open('ssafy.txt','w') as f:
    f.writelines(['0\n','1\n','2\n','3\n'])


#read()
with open('with_ssafy.txt', 'r') as f:
    all_text = f.read()
    print(all_text)

with open('ssafy.txt', 'r') as f:
    all_text1 = f.read()
    print(all_text1)

#readlines() : 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 list로 만들어냄.

with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        #print(line.strip())
        print(dir(line))

