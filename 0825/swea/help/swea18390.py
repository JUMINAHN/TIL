import sys

sys.stdin = open('../stack2-1/input18390.txt')

def op_rate(a): #연산자 순위
    if a in ('+', '-'):
        return 1
    elif a in ('*', '/'):
        return 2 #우선순위가 큰 것
    else :
        return 0 #(의 경우 0-> 내부에서

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    #print(arr)
    #keypoint 자체가 -> (, )를 별도로 구분하는 것


    #이러기 위해서 빈 stack과 출력값을 담을 change
    stack = [] #연산자를 담을 곳
    change = [] #피연산자를 담을 곳
    #먼저 후위표기식으로 변환
    for a in arr:
        if a.isdecimal(): #a가 숫자라면 change에 넣자
            change.append(a)
        elif a == '(':
            stack.append(a) #(과 )자체를 하나로 둔다.
        elif a == ')':
            while stack and stack[-1] != '(': #stack에 (가 아닐때까지
                change.append(stack.pop())
            stack.pop() #)일떄 pop
        else : #아니라면 stack에 넣자
            #그리고 '('를 만날때
            while stack and op_rate(stack[-1]) >= op_rate(a) : #stack에 차있을 경우, 그리고 우선순위가 작을 경우 pop, a가 더 작을경우 큰 애들을 pop해줘야함
                # if stack[-1] == '(' : #????????? 여기서 pop을 하고 '('에 관련된 것을 없애고 싶은데 계속 list out of idx가 더
                #     #여기서 바로 pop을 하면 첫번째 (조차도 들어가지 않는 문제가 발생하고, pop을 하지 않으면  * 뒤에 (도 pop이되지 않음
                #     break
                    change.append(stack.pop()) #근데 )까지도 APPEND되게 되는

            #근데 스택이 비어있을 때 넣고 싶다.
            stack.append(a)

    #이랬는데도 스택에 남을 수 있기 떄문에 그것까지 빼서 change에 넣어준다.
    #print(stack)
    while stack:
        change.append(stack.pop())
    print(change)