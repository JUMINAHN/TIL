pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

#위치 인자 먼저
def create_data(subject, day, title=None): #인자로 과목, 일차, 제목을 받을 수 있도록
    global pro_num
    pro_num += 1
    #data = {'과목' : subject, '일차' : day, '제목' : title, '문제 번호' : pro_num}
    data = {}
    data['과목'] = subject
    data['일차'] = day
    data['제목'] = title
    data['문제번호'] = pro_num
    return data

result_1 = create_data(global_data['subject'], global_data['day']) #매개변수를 key에 할당
print(result_1)

result_2 = create_data('web', 1, 'web 연습하기')
print(result_2)

result_3 = create_data(global_data['subject'], global_data['day'], global_data['title'])
print(result_3)





# pro_num = 1000
# global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

# def create_data():
#     pass

# result_1 = create_data() 
# print(result_1)

# result_2 = create_data()
# print(result_2)

# result_3 = create_data()
# print(result_3)
