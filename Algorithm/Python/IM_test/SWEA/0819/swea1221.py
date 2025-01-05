import sys

sys.stdin = open('input1221.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #현재 문자열의 길이는 문자 타입으로 받아짐
    test_case, str_length = input().split() #문자의 길이 -> str_length만 사용할 것
    word = list(input().split()) #SVN FOR ZRO NIN FOR EGT EGT TWO FOR
    #해당 내용을 정렬하기 위해선 먼저 숫자로 변환시켜줘야 함
    dict_word = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5 , 'SIX' : 6,
                 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}

    change_word = [] #변환한 숫자를 담을 리스트
    for w in word:
        change_word.append(dict_word.get(w))
    #print(change_word) #확인

    #선택 정렬_idx 접근
    #문자열인 str_lenght를 숫자로 변환
    str_length = int(str_length)
    for i in range(str_length-1):
        min_idx = i
        for j in range(1+i, str_length):
            if change_word[min_idx] > change_word[j]:
                min_idx = j
        change_word[i], change_word[min_idx] = change_word[min_idx], change_word[i]
    #print(change_word)

    dict_word2 = { 0 : 'ZRO', 1 : 'ONE', 2 : 'TWO', 3 : 'THR', 4 : 'FOR', 5 : 'FIV' , 6 : 'SIX' ,
                  7 : 'SVN',  8 : 'EGT', 9 : 'NIN'}
    #바뀐 내용을 다시 dictionary로 바꿔준다.
    final_word = []
    for c in change_word:
        final_word.append(dict_word2.get(c))
    print(test_case)
    print(*final_word)