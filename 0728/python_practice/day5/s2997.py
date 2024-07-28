original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"' #잘못된 문장
word = '1ㄴ2ㄹ3ㅓ4ㅅ5' #제거할 대상이 작성된
arr = [] #빈 리스트
new_arr = [origin for origin in original_word]
arr.extend(new_arr)
print(arr)

#문장에서 잘못된 내용을 제거하는 함수 작성
def restructure_word(word): #인자로 넘겨받은 word 문자열을 순회
    for w in word: #arr에서 불필요한 문자열 제거 --> 요소 확인 후 제거 remove(w)
        if w.isdecimal() :
            for _ in range(int(w)):
                arr.pop()
        else :
            arr.remove(w)
    return arr
result = restructure_word(word)
print(result)
print("".join(result)) #list type

