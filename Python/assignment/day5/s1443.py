
#대문자 만드는 메서드
# def capitalize_words(word):
#     return word.title()
'hello'.capitalize()

def capitalize_words(word): #capital 대문자 만들기
    result = list(word.split())
    for r in result:
        print(r.capitalize(), end=" ")

result = capitalize_words("hello, world!")



# result = capitalize_words("hello, world!")
# print(result)
