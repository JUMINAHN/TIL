#append == push, pop을 직접 사용하는 것은 용량을 많이 잡아먹을 수 있는 부분임을 알고 있을 것
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
print(stack) #최하단 원소부터 출력

