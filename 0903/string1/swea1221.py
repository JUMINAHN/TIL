import sys

sys.stdin = open('input1221.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    language = {'ZRO' : 0, 'ONE' : 1, 'TWO': 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}
    #문자열을 정렬해서 작은값부터 정렬해라
    test_case, size = input().split() #두개로 나눠서 전달받음
    size = int(size) #숫자로 변환해주고
    data = list(input().split()) #문자열을 받음

    ch_word = []
    for d in data:
        ch_word.append(language.get(d)) #data를 받아서 ch_word에 담기
    #정렬
    #선택 정렬해보기
    for i in range(size-1):
        min_idx = i
        for j in range(i+1, size):
            if ch_word[min_idx] > ch_word[j]:
                min_idx = j
        ch_word[min_idx], ch_word[i] = ch_word[i], ch_word[min_idx] #위치 바꿔주기
    #print(ch_word) -> 여기에 바뀐데이터 너어주고
    #다시 변환하기
    re_language = {0: 'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}
    result = []
    for ch in ch_word:
        result.append(re_language.get(ch))
    #print(result)
    print(f'#{tc}')
    print(*result)