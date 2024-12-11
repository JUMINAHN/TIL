# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    #사용자로부터 이름과 나이를 입력받는 메서드
    #초기화 메서드 없이 일반 메서드로 전달받아서 넣는 방법? -> 받는 것을 초기값이 아니라 밑에서 받으면 안되나?
    def get_user_info(self): #여기서 잘못된 형식으로 입력했을 경우 예외를통해 적절한 안내 메시지를 
        try :
            self.name = input('이름을 입력하세요 : ')
            self.age = int(input('나이를 입력하세요 : ')) #나이를 숫자로 입력해야 합니다
            self.information = input('사용자 정보 : ') #사용자 정보가 입력되지 않았습니다.
        except ValueError :
            print('나이는 숫자로 입력해야 합니다.')
            print('사용자 정보가 입력되지 않았습니다.')
        else :
            print(f'이름 : {self.name}\n나이 : {self.age}')

    def display_user_info(self): #입력된 이름과 나이를출력하는 메서드
        pass


user = UserInfo()
user.get_user_info()
user.display_user_info()
