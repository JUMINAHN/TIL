# 아래 함수를 수정하시오.

#print('hello'.capitalize())
#'ehllo, hello'.split()

def capitalize_words(word):
    temp_list = word.split()
    new_list = []
    for temp in temp_list:
        temp = temp.capitalize()
        new_list.append(temp)
    return " ".join(new_list)
 #capitalize는 새로운 문자열을 반환하는 메서드이다.


result = capitalize_words("hello, world!")
print(result)
