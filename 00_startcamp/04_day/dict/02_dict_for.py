lunch = {
    '중국집' : '01-123-4567',
    '일식집' : '02-890-1234',
    '한식집' : '03-567-8901'
}
#기본활용
for key in lunch:
    print(key)
    print(lunch[key])


#.items() 활용

for key, value in lunch.items():
    print(key, value)

# value만 가져오기 .values()
for value in lunch.values():
    print(value)

#key 만 가져오기 . keys()
for key in lunch.keys():
    print(key)