data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'

#대문자이거나 공백인경우만 출력
for data in data_1:
    if data.isspace() or data.isupper(): #공백인 경우 -> isspace() --> '' in data_1
        print(data, end = "") 
print()


data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
#글자들이 위치한 것을 찾기 --> index, find 메서드 
arr = []
arr.append(data_2.find('내'))
arr.append(data_2.find('힘'))
arr.append(data_2.find('들'))
arr.append(data_2.find('다')) #find -> index 번호가 담길 것
print(arr)
arr.sort()
print(arr)
#find가 index로 찾는 것 --> !!
for a in arr:
    print(data_2[a], end="")

# data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
# data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'