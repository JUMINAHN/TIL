# 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하기


# # 3. setdefault 메서드를 사용한 방법
def dict_invert(input_dict):
    new_dict = {}
    for k,v in input_dict.items():
        new_dict.setdefault(v, []).append(k)
    return new_dict


print(dict_invert({1: True, 2: True, 3: True}))  # {True: [1, 2, 3]}