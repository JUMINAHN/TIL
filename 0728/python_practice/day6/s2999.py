data = {
    '이름': '키위',
    '종류': '새',
    '원산지': '호주' 
}
print(data.items())
print(data.values())
data.get('without', 'unknown')


plus_data = {
    '종류': '과일',
    '가격': 30000
}
for k,v in plus_data.items():
    data.update({k:v})

#for k,v in plus_data.items():
#    data.setdefault(k,v)
print(data)