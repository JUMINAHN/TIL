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

class Other(BaseModel):
    TYPE = 'Other Model'
    def __init__(self, data_type, title, content, created_at, updated_at):
        super().__init__(data_type, title, content, created_at, updated_at)
    def save(self):
        print('데이터를 다른 장소에 저장합니다.')

class ExtendedModel(Novel, Other): #다중상속
    PK = 1 
    # 생성자 여러개 가능?
    # 나는 궁금한게 Other의 type이 지금 내가 원하는거라서 -> Other에 먼저가면 복잡한 접근이 필요없을 것 같아 이렇게 접근했는데
    # 매개변수 개수가 다르고 novel이 author 매개변수를 하나 더 가지고 있어서 경로를 타고 오르는 과정에서 에러가 발생하는 것 같음
    def __init__(self, data_type, title, content, created_at, updated_at, author, extended_type):
        super().__init__(data_type, title, content, created_at, updated_at, author)
        self.extended_type = extended_type

    #클래스 변수라서 -> cls는 메서드 생성(?) -> 클래스 메서드 사용시 pk에 접근 가능..?
    def display_info(self): #클래스 변수PK와 클래스 변수 TYPE, 그리고 인스턴스 변수 extended_type을 출력
        print(f'PK : {ExtendedModel.PK}, TYPE : {ExtendedModel.TYPE}, Extended Type : {self.extended_type}')
    def save(self):
        print('데이터를 확장해서 저장합니다.')

extended_instance = ExtendedModel('소설', '홍길동', '고전 소설', 1618, 1692, '허균', 'Extended Type')
extended_instance.display_info()
extended_instance.save()
