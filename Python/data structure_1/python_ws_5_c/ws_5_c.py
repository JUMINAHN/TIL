def restructure_word(word, arr): 
    for w in word:
        if w.isdecimal() :
            for i in range(int(w)):
                arr.pop()
        else :
            arr.remove(w) #remove 너무 많이 순회해서 불필요한 값까지 제거 되는 문제!!
    return arr



original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"' 
original_word = list(original_word) 
arr = []
arr.extend(original_word)
print(arr)

word = '1ㄴ2ㄹ3ㅓ4ㅅ5' #제거할 대상

result = restructure_word(word, arr)
print(result)
print(''.join(result))


