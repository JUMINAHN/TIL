#유저가 입력한 정보 검사하는 프로그램 생성
#신규 아이디 생성시, 아이디 비번 모두 빈값이 입력되는 것 방지
#입력 정보 user_data == dictionary일 때 입력한 아이디 중 하나라도 비어있으면 false 아니면 True

# if (user_data.keys() == None) or (user_data.values() == None): #key 기준 --> get에 키가 없어도 되는지
#key가 비어있는 것 검증 --> key --> dict기준이 무엇으로 돌아가는지
#'' in user_data
#key를 무엇으로 잡으면 좋을 지..
def is_user_data_valid(user_data):
    if '' in user_data.keys() or '' in user_data.values(): #key 기준 --> get에 키가 없어도 되는지
        print(False)
    else :
        print(True)

id = input('아이디를 입력하세요 : ')
pw = input('pw를 입력하세요 : ')
user_data = {id : pw}
is_user_data_valid(user_data)
