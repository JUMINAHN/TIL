import sys

sys.stdin = open('input18224.txt')

#짝이면 1, 아니면 0
#{}, ()
T = int(input()) #testcase 들어갈 수
for tc in range(1, T+1):
    #push pop함수 만들기
    def my_push(item, size): #넣을값, 길이
        global top
        if top == size:
            return
        else :
            top += 1
            stack[top] = item

    def my_pop():
        global top
        if top == -1 : #0보다 더 작은 -1에 idx를 접그하려고 하면
            return 0 #idx 0을 도출하고
        else :
            top -= 1
            return stack[top + 1]

    arr = list(map(str, input())) #{}랑 ()말고 remove해도 될 것 같은데 생각처럼 안먹힌다.
    new_arr = [] #그래서 새로운 배열에 필요한 값만 담았다.
    top = -1
    stack = [0] * len(arr) #arr만큼의 새로운 배열을 만든다.
    #stack2 = [0] * len(arr)
    for i in range(1, len(arr)):
        if arr[i] == '(' or arr[i] == ')' or arr[i] == '}' or arr[i] == '{':
            new_arr.append(arr[i])
    #print(new_arr)
    result = 1
    for new in new_arr:
        if new == '(' or new == '{': #어쩄든 개수가 안맞을거니까?
            my_push(new, len(new_arr))
        elif new == ')' or new == '}':
            if top == -1:
                result = 0
            my_pop()

    if top != -1:
        result = 0
    print(f'#{tc} {result}')





