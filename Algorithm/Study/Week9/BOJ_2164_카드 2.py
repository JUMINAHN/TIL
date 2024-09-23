from collections import deque

N = int(input()) #6
card = deque()
for i in range(1, N+1):
    card.append(i)
#print(card)

#짝수는 뒤로
for i in range(len(card)):
    if len(card) == 1:
        break
    card.popleft()
    card.append(card.popleft())
print(*card) #unpacking