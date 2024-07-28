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
for dic_data in data : #dictionary
    print(f'{key_list[0]} 은/는 {dic_data.get("name", "unkwnow")}')
    print(f'{key_list[1]} 은/는 {dic_data.get("company", "unkwnow")}')
    print(f'{key_list[2]} 은/는 {dic_data.setdefault("is_collapsible", "unkwnow")}')
    print()