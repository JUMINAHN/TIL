data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
# 대문자이거나 
# 공백인 경우,, 
for data in data_1:
    if data.isupper() or data.isspace():
        print(data, end = "")


print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.
#find 메서드를 통해서 원하는 index찾기
arr.append(data_2.find('내'))
arr.append(data_2.find('힘'))
arr.append(data_2.find('들'))
arr.append(data_2.find('다'))
print(arr)
arr.sort()
print(arr)

for find_num in arr:
    print(data_2[find_num], end = "")

# arr에 있는 순서를 반환하는 것 -> index()는 특정값의 위치를 찾는 것이고
# 인덱스로 list 내부 찾기 --> 단순 접근

# for구문 사용하지 않고 그냥 접근해보기
# arr안에 이제 내가 찾고자 하는 숫자가 있음
# print(data_2[arr[0]])
# print(data_2[arr[1]])
# print(data_2[arr[2]])
# print(data_2[arr[3]])
