# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self): #이름과 나이를 입력 받음 --> 내부적으로
        try :
            self.name = input('이름을 입력하세요 : ') 
            self.age = int(input('나이를 입력하세요 : '))
            self.info = input('사용자 정보 : ')


            # name = input('이름을 입력하세요 : ') 
            # age = int(input('나이를 입력하세요 : '))
            # info = input('사용자 정보 : ')

            user_data = {'name' : self.name, 'age': self.age}
            self.user_data.update(user_data)
        
        except:
            print('나이는 숫자로 입력해야 합니다.')
        
    def display_user_info(self):
        try :
            if self.info == '':
                print(self.info)
        except:
            print('사용자 정보가 입력되지 않았습니다.')
        else :
            print(f"이름 : {self.user_data['name']}\n나이 : {self.user_data['age']}")

user = UserInfo()
user.get_user_info()
user.display_user_info()





# 아래 클래스를 수정하시오.
# class UserInfo:
#     def __init__(self):
#         self.user_data = {}

# user = UserInfo()
# user.get_user_info()
# user.display_user_info()

