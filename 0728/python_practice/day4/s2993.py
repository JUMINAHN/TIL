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
#for 과 if를 사용해서 각각 적절한 값이 출력되도록
#for문
for food in food_list:
    if food['이름'] == '자장면':
        print(f'{food["이름"]}엔 고춧가루지')
    elif food['이름'] == '토마토':
        food['종류'] = '과일'
    print(f"{food['이름']} 은/는 {food['종류']} (이)다") #SyntaxError: f-string: unmatched '['
print(food_list)



# food_list = [
#     {
#         '종류': '한식',
#         '이름': '잡채'
#     },
#     {
#         '종류': '채소',
#         '이름': '토마토'
#     },
#     {
#         '종류': '중식',
#         '이름': '자장면'
#     },
# ]