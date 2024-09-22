#파이썬으로 큐를 구현할 떄는 collections 함수를 사용하는 것이 좋다.
#deque는 리스트 자료형에 비해 효율적이며 queue라이브러리를 이용하는 것보다 더 간단하다.

from collections import deque

#단, deque를 사용할 list이름을 선언 해야함
queue = deque() #list 형식으로 deque()선언

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
print(queue) #출력형식에 나타나는 deque는 신경쓰지 말 것
#deque([3, 7, 1, 4])

# queue = []
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.pop(0)
# queue.append(1)
# queue.append(4)
# queue.pop(0)
# print(queue)
