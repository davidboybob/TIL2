import os


os.chdir(r'C:\Users\student\Desktop\TIL\00_startcamp\02_day\chage_filenames')

#2. 현재 폴더 안에 모든 파일 이름을 수집

filenames = os.listdir('.')
# print(filenames)

#3. 각각의 파일명을 돌면서 수정한다.
# for filename in filenames:
#     os.rename(filename, f'SAMSUNG_{filename}')

#4. SAMSUNG 을 SSAFY로 변환

for filename in filenames:
    os.rename(filename, filename.replace('SAMSUNG_', 'ssafy_'))