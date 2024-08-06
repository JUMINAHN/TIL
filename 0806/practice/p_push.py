#push함수 사용
#push 함수를 이해하기 위해 append와 비교

#1. append사용
s = []
s.append(1)
s.append(2)
print(s) #빈 배열에 원하는 숫자가 들어간다.

#하지만 대부분 배열은 크기가 유도적이지 않다는 특징이 있다.
#따라서 다양한 언어의 자료 접근을 위해서 배열의 크기를 size를 기반으로 고정시킨다.
#2. push --> append용으로 사용할 함수 정의
def my_push(item ,size): #내가 넣을 값과 배열의 크기 호출
    global top
    top += 1 #0으로 바뀐다.
    if top == size:
        print('overflow') #디버깅용 메세지 추가
        return #구문을 빠져나간다 -> 돌려줄 것이 없다
    else :
        stack[top] = item #stack에 내가 원하는 것을 적어준다.
        #즉 stack의 0번째 idx에는 내가 원하는 item 값이 들어가게 된다.

size = 10
stack = [0] * size
top = -1 #시작할 곳
my_push(3, size) #인덱스에 3을 넣겠습니다.
print(stack) #3이 들어간 것을 확인할 수 있다.