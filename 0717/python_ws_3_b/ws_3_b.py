pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}


def create_data(subject, day, title=None):
    data = {} 
    global pro_num
    pro_num += 1
    data['과목'] = subject 
    data['일차'] = day 
    data['제목'] = title 
    data['문제 번호'] = pro_num 
    return data 


result_1 = create_data(global_data['subject'], global_data['day']) #인자 -> title에 대한 값이 None인데 받아야하나?
print(result_1)

result_2 = create_data(subject='web', day=1, title='web 연습하기')
print(result_2)

result_3 = create_data(global_data['subject'], global_data['day'], global_data['title'])
print(result_3)


####
# pro_num = 1000
# global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

# #매개변수
# def create_data(subject, day, title=None):
#     data = {} #함수 내부에서 data변수를 작성한다.
#     #data 문제번호 키에 할당되는 값은 global에 정의된 pro_num에 1을 더한 것
#     #그러면 이 data에 argument들이 들어가야 한다는 것인데
#     #dict에 개별적으로 할당을 받아야한다는 것인데 -> *kwargs를 사용하지 않는 것이다
#     global pro_num
#     pro_num += 1
#     data['과목'] = subject #global_data['subject']
#     data['일차'] = day #global_data['day']
#     data['제목'] = title #None으로 받을 것
#     data['문제 번호'] = pro_num #변수에 각 1을 더한 값이 되어야 함 
#     #여기서 error발생 --> key error

#     #pro_num이 계속해서 증가해야함 
#     return data #dictionary 타입 자체를 반환

# #인자로 과목, 일차, 제목을 받을 수 있도록 매개 변수 설정

# #문자열 python과 정수 3을 순서대로 담아 호출한다.
# result_1 = create_data(global_data['subject'], global_data['day']) #인자 -> title에 대한 값이 None인데 받아야하나?
# print(result_1)

# #키워드 인자를 작성한다.
# result_2 = create_data(subject='web', day=1, title='web 연습하기')
# print(result_2) #문제번호

# result_3 = create_data(global_data['subject'], global_data['day'], global_data['title'])
# print(result_3)