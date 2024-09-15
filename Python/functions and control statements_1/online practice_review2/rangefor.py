AA = 'hello'
#enumerate * continue사용
#for index, i in enumerate(AA):
#    if index % 2 == 0:
#        continue
#    print(i)

# range를 사용해보자
#자 생각한대로 이렇게 하면 숫자가 나옴
for i in range(len(AA)): 
    print(i)

# 문자열을 하나씩 접근하기 위해선?
# iterable의 특징을 기억하고, '인덱스'로 접근할 수 있음을 잊지 말자
print('0번', AA[0])
print('2번', AA[2])
print('4번', AA[4])

# iterable로 인덱스를 []을 사용해서 접근할 수 있음을 잊지 말자
for i in range(0, len(AA), 2):
    print(AA[i])

# list slicing으로 접근하느 방법
AA = 'hello'
for a in AA[::2]:
    print(a)