food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# f스트링 사용 주의
# for문
for food in food_list:
    if food['이름'] == '토마토':
        food['종류'] = '과일'
    elif food['이름'] == '자장면':
        print(f'{food["이름"]}엔 고춧가루지')
    print(f'{food["이름"]} 은/는 {food["종류"]} (이)다.')
print(food_list)

# while문
number = 0
while len(food_list) != number :
    if food_list[number]['이름'] == '토마토':
        food_list[number]['종류'] = '과일'
    elif food_list[number]['이름'] == '자장면':
        print(f'{food_list[number]["이름"]}엔 고춧가루지')
    print(f'{food_list[number]["이름"]} 은/는 {food_list[number]["종류"]} (이)다.')
    number = number + 1
print(food_list)