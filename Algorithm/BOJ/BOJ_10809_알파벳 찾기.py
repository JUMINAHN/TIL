#단어 포함되어 있는 경우 처음 등장하는 위치
#포함되어 있지 않은 경우 -1을 출력
#단어 S가 주어진다 == 소문자로

#출력 형식
#a..b.....z까지의 위치를 공백으로 구분해서 출력
#포함되어있지 않다면 -1을 출력, 단어의 첫번째 글자는 0번째 -> idx 그자체
#처음 등장하는 위치

#a부터 z까지 다 돌면서
input_data = input() #baekjoon 그자체
alpha = 'abcdefghijklmnopqrstuvwxyz' #이 alpha를 모두 돈다.

for a in alpha:
    if a not in input_data: #input_data에 포함되지 않는다면 -1을 출력
        print(-1, end= " ")
    else : #그게 아니라면 위치 출력 -> 특정 위치 idx 출력
        # 즉 a가 input_data안에 있다는게 전제가 되는 것 -> 즉 input_data의 몇번쨰 위치인지 출력하면 되는 것
        #for data in input_data: #몇번쨰 idx? -> find
        idx_num = input_data.find(a) #이게 몇번째 idx인지?
        print(idx_num, end= " ")