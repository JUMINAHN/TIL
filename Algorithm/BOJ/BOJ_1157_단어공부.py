#대소문자 단어로 주어졌을 떄 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램 작성
#대문자와 소문자를 구분하지 않음 -> 대문자로 출력할거니까 소문자를 모두 대문자로 변환
#가장 많이 사용된 알파벳의 대문자 출력
#단 가장 많이 사용된 알파벳이 여러개 존재하는 경우에는 ?출력

#upper 사용하면 되지 않을까? => python 내장 모듈 검색 후 사용
#upper는 새로운 타입 반환하는 거라서 새로운 데이터를 생성함
Big = []
arr = list(input()) #mississipi
for a in arr:
    Big.append(a.upper())

#각각 count
#그러면 모두 순환하는 과정에서 가장 큰 값을 넣고 -> 개수를 기준으로
#개수도 따로 확보해놓는다.
#순환하는 것중에서 가장 큰 값이 동일하면 ?를 출력하고
#print(Big) == 변환 확인 됨

#인덱스 0을 A로 두고 ...어쩌구를 Z로 두는 케이스
#딕셔너리 카운트
alpha = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0,
         'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0,
         'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
#그래서 루프를 순회하면서 .get으로 받아와서 count를 높인다.
for b in Big: #big에 담음
    num = alpha.get(b) #받아서
    num += 1 #1을 올리고 -> 다시 집어 넣기
    alpha[b] = num #해당 값을 넣어준다.
#print(alpha) #제대로 담기는 것 확인

#그중에서 가장 큰 것 뽑기
#max_num = max(alpha) #그냥 제일 뒤에있는 값이 뽑힌다.
max_num = 0 #가장 큰 값 뽑아서 돌릴 것
max_alpha = 'A' #그냥 A로 설정하고
result = 0 #이것도 숫자가 담길것인지만 0으로 기본 값 설정하고
for b in Big:
    num = alpha.get(b)
    if max_num < num:
        max_num = num # 다돌고
        max_alpha = b #b를 담고
#가장 큰 값을 담기만 한 것
for b in Big:
    if b == max_alpha: #같은 값이면 무시하고
        continue
    if max_num == alpha.get(b): #가 더 크다면 #크거나 같다면 -> 크거나 같은게아니라 같다면
        print('?')
        break
else :
    print(max_alpha)

"""
max_count = 0
max_alpha = Big[0] #일단 Big의 0번째 idx로 확보
result = 0 #일단 빈값 하고 싶은데 숫자 0으로 놓아두기
for b in Big:
    num_count = Big.count(b)
    #근데 만약 지금 b가 max count랑 같다면?
    if max_count == num_count: #모두 다 돌아야되지 않을까 -> 중간에 break를 걸려고 했는데
        #max값이 반영되지 않았을때 그럴 확률이 있을 것 같아서
        #지금 코드 처럼 작성하면 똑같은 a값이라서 ?가 뜨는 문제가 발생
        result = '?'
    else : #아닐떄의 값 넣기
        result = 0
        if max_count < num_count:
            max_count = num_count
            max_alpha = b #b를 넣는다
            result = max_alpha #result에 바뀐 값 반영

print(result)
"""
