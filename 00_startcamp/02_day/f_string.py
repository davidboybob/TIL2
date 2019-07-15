# name = '김준호'
# print(f'안녕하세요, {name} 입니다.')

# # 점심메뉴 추천
import random

# menu = ['부대찌개', '소고기','카레']
# lunch = random.choice(menu)

# print(f'오늘의 점심은 {lunch}')


numbers = range(1, 46)
lotto = random.sample(numbers, 6)

print(f'오늘의 로또 당첨번호는 {sorted(lotto)}입니다.')

