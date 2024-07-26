data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'

# data_1을 순회하며 대문자이거나 공백이 ' '인 경우만 출력한다
# 공백 확인 메서드 'isspace()' 
for data in data_1:
    if data.isupper() or data.isspace():
        print(data, end = "")
print()


data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
arr.append(data_2.find('내'))
arr.append(data_2.find('힘'))
arr.append(data_2.find('들'))
arr.append(data_2.find('다'))
print(arr)

arr.sort() 
print(arr) #5, 12, 29, 37

for ar in arr:
    print(data_2[ar], end = "")

# 각 요소에 위치한 문자열 출력


