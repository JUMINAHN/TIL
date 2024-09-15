class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
    
class Other(BaseModel): #Type클래스 변수값을 -> OtherModel로 변경, #save 출력 내용을 변경
    TYPE = 'Other Model' #생각해보니 그냥 OtherModel을 선언하면 되는 것이었다...
    def __init__(self, data_type, title, content, created_at, updated_at):
        super().__init__(data_type, title, content, created_at, updated_at)
        #OtherModel로 변경 --> 클래스 전체 타입을 바꾸겠다는 것인지?? --> 클래스에 직접접근..?
        #근데 클래스 변경이 Other가 가지고 있는 부모에 대한 궁극적인 클래스만 변경되는 것인지 설계도에도 변경되는 것인지?
        #그니까 class로 변경을 하면 -> 전반적으로 변경되는 것을 확인할 수 있음

    def save(self):
        print('데이터를 다른 장소에 저장합니다.')
    pass

# 다중 상속을 활용하여 새로운 모델 클래스를 만들고, 요구 사항을 만족하는 코드를 작성하세요
class ExtendedModel(Novel, Other):
    PK = 1 # 새로 할당 --> 단순 PK만 선언
    #근데 상속이 되면서 초기화가 됨에 따라 이제 객체의 값이 증가하게 나오는 것인지?
    def __init__(self, data_type, title, content, created_at, updated_at, author, extended_type):
        super().__init__(data_type, title, content, created_at, updated_at, author)
        self.extended_type = extended_type

    def display_info(self) :
        #클래스 변수 PK클래수 변수 Type, 인스턴스 변수 extended_Type을 출력
        #근데클래스 변수 자체에 접근 해야하기 때문에..
        print(f'PK : {ExtendedModel.PK}, TYPE : {ExtendedModel.TYPE}, Extended Type : {self.extended_type}')

    def save(self):
        print('데이터를 확장해서 저장합니다.')

print('ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출')
model = ExtendedModel('소설', '홍길동', '고전 소설', 1618, 1692, '허균', 'Extended Type') #다른거 내부로 적어야 함
model.display_info()
model.save()
