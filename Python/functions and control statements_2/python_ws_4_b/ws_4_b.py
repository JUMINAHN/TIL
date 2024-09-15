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

number = 0
while number != 3:
    name = food_list[number]['이름']
    if name == '토마토':
        food_list[number]['종류'] = '과일'
    if name == '자장면':
        print(f'{name}엔 고춧가루지')
    category = food_list[number]['종류']
    print(f'{name} 은/는 {category} (이)다.')
    number = number + 1
print(food_list)

for food in food_list: 
    name = food['이름'] 
    category = food['종류']
    if name == '토마토':
        food['종류'] = '과일' 
    elif name == '자장면':
        print(f'{name}엔 고춧가루지')        
    print(f'{name} 은/는 {category} (이)다.')
print(food_list) 

#새로 변수명을 선언했다면 그 변수명이 아닌 원래 값 자체를 바꿔야 한다