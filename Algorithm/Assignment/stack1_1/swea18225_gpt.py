import sys

sys.stdin = open('input18225.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(map(str, input()))
    stack = [0] * len(data)
    top = -1 #맨 위상단
    def my_push(item, size):
        global top
        if top == size:
            return #초과함
        else:
            top +=1 #처음은 0
            stack[top] = item

    def my_pop(): #pop
        global top #현재의 top 위치 -> idx 0에서 시작
        if top == -1 : #0보다 더 작은 stack에 없다면
            return 0 #0을 반환
        else :
            top -= 1
            return stack[top+1] #마이너스하기 전 현 스택에 대한것을 반환 --> 기준은 지금

    for char in data:
        if top == -1 or stack[top] != char: #같은게 아니면 --> data -1이런게 아니라
            my_push(char, len(data)) #추가하고
        else: #그게 아니면 뺸다
            my_pop()

    remaining_length = top + 1 #혹시나 남아있는 idx가 있따면?
    #top은 가장 위에 있는 idx 요소를 가리킨다 -> 따라서 실제 요소의 개수는 top + 1이기 때문이다.

    #len을 사용하지 않는 이유는 스택의 전체 배열 길이를 반환하는 것이기 떄문이다
    #실제 요소의 개수와 다르기 떄문에 저장된 요소의 개수를 확인하기 위해서 top+1를 해야한다
    print(f'#{tc} {remaining_length}') #len stack을 하면 그냥 배열 전체가 나오고 내가 언하는 값이 안나옴



