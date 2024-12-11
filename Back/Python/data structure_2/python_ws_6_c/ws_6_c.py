#다수의 dict을 보유한 list
data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

#키 목록이 담긴 리스트
key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for sub_data in data : #sub_data 자체가 dict
    for key in key_list: #key 하나씩
        #sub_data.get(key, 'unkwnow')
        sub_data.setdefault(key, 'unkwnow') #setdefalt
        print(f"{key} 은/는 {sub_data.get(key)} 입니다.")
    print()