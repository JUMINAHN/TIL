#reversed는 iterable에만 사용됨
#문자열로 만들기 위해선 join 메서드로 활용해주면된다
def reverse_string(result):
    result = reversed(result) #reversed 자체는 객체로 반환됨
    return ''.join(result)

result = reverse_string("Hello, World!")
print(result)  


