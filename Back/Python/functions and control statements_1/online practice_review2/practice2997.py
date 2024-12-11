def restructure_word(word, arr): 
    for w in word:
        if w.isdecimal() : 
            for _ in range(int(w)):
                arr.pop()
        else :
            arr.remove(w)
    return arr 


original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"' 
original_word = list(original_word) 
arr = []
arr.extend(original_word)
print(arr)


word = '1ㄴ2ㄹ3ㅓ4ㅅ5' 
result = restructure_word(word, arr)
print(result)
print(''.join(result))


