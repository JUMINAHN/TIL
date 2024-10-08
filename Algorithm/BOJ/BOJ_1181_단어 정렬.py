#길이가 짧은 것부터
#사전 순으로 -> 오름차순
#중복된 단어 제거
N = int(input()) #개수
data_list = [input() for _ in range(N)] #13개의 데이터가 input됨
data_list = set(data_list)
data_list = list(data_list)
#해당 부분을 정렬
#sort 키 사용
data_list.sort() #정렬을 하고 -> 또 길이를 기준으로 정렬
data_list.sort(key=len) #길이를 기준으로 -> sort를 길이를 기준으로 정렬 == key값 사용
for d in data_list:
    print(d) #길이를 기준으로 단순 출력됨 == 단순 중복 제거를 하니까 정렬이 됨