#pop은 원래 python에서 사용하는 pop의 구조와 같다고 보면 된다.
#따라서 해당 내용을 그대로 코드로 구현하자
#append와 유사하게 접근하면 된다.
#다만 여기서 pop은 뒤에있는 것을 먼저 튕겨내는 것이기 때문에 top의 값을 지정함에 유의해야 한다.

def my_pop(): #매개변수는 없다. 그 이유는
    global top
    if top == -1 :
        return 0 #0번쨰 idx가 마지막이기 떄문에 그뒤로 갈 수 없다.
    else : #append와 다르게 여기서 진행하는 이유?
        top -= 1 #total -> pop해주면서 1의 idx가 감소됨
        return stack[top+1] #다만 빼기 전의 마지막 내용을 반환한다.
        #위에서 top -1을 해주었기 떄문에

size = 10
stack = [0,1,2,3,4,5,6,7,8,9]
top = 9 #9인 이유는 총 idx의 길이가 9이기 때문이다. (idx는 0부터 시작)
result = my_pop()
print(result)
print(stack)