# 아래 클래스를 수정하시오.
class StringRepeater:
    def __init__(self) : #초기값 매개변수 없음
        pass
    
    def repeat_string(self, number, string_s) : #self 선언하기
        for _ in range(number):
            print(string_s)


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")



# # 아래 클래스를 수정하시오.
# class StringRepeater:
#     pass


# repeater1 = StringRepeater()
# repeater1.repeat_string(3, "Hello")