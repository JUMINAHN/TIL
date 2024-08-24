import sys

sys.stdin = open('input4865.txt')
#테스트 케이스 개수
#count 정렬..
T = int(input())
for tc in range(1, T+1):
    #str1에 포함된 글자들이 str2에 몇개있는지 찾고, 가장 많은 글자의 개수 출력
    #str1이 ABCA, str이 ABABCA인경우 ABCA중의 단어가 있는 A가 ABABCA에 있으며 3개가 있는 것을 알 수 있다.
    #dictionary를 이야기 했는데 중복되는 단어는 굳이 str1에서 찾을 필요가 없지 않을까?
    #dictionary 짜피 중복 제거됨 -> 키가 여러개일 수 없음

    str1 = list(input()) #카운트 키를 받을 내용
    str2 = list(input()) #카운팅할 내용

    find_key = {} #키는 넣고, 값은 0으로 한다음에 그 부분을 카운팅
    for s1 in str1:
        find_key.setdefault(s1, 0)
    #print(find_key) : 원하는 값 들어간 것 확인했다.
    #value에 값을 집어넣기 위해서 키를 바탕으로 접근한다.
    #print(find_key)
    for s2 in str2:
        if find_key.get(s2) == None:
            continue
        result = find_key.get(s2)
        result += 1
        find_key[s2] = result #그냥 키 자체에 값을 넣는 방법이 생각나서 이렇게 바꾸었다.
    #자 이 value에서 가장 큰 것을 골라야 한다.
    max_val = 0
    for num in find_key.values():
        if max_val < num:
            max_val = num
    print(f'#{tc} {max_val}')
