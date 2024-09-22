#알파벳 소문자로 이루어진 N개의 단어 조건에 맞게 정렬
#길이가 짧은 것부터
#길이가 같으면 사전 순으로
#중복된 단어는 하나만 남기고 제거해야 함
N = int(input())
arr = [input() for _ in range(N)] #개수만큼 input됨
#arr.sort() #단순 sort를 진행한다면? -> abcde~순서대로 진행됨
#해당 메서드 유용하게 사용하기
#key=len, reverse 같은 것 -> 내림 차순 정렬
#중복되는 것 set으로 제거
arr = set(arr)
arr = list(arr)

#먼저 중복되는 값 삭제하고 정렬
arr.sort()
arr.sort(key=len) #list 값들의 length에 따라 정렬 -> wait랑 wont, more파트 정렬이 안되어있음..
#print(arr) #그냥 단순 출력하면 됨

for a in arr:
    print(a)