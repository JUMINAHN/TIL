pro_num = 1000 #기본 셋팅 값
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'} #기본 셋팅 값

def create_data(subject, day, title=None): #호출되면 인자들이 담기게 됨
    #함수가 만들어질 떄마다 값이 바뀌려면
    global pro_num
    pro_num += 1
    data = {}
    data['과목'] = subject #값으로 들어온다
    data['일차'] = day
    data['제목'] = title
    data['문제 번호'] = pro_num
    return data

result_1 = create_data(global_data['subject'], global_data['day'])
print(result_1)
