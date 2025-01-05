#내 풀이
'''
123402
'''
arr = list(input()) #[1,2,3,4,0,2]
N = len(arr)
#print(N) : 개수 확인
x_sum = y_sum = 0
for x in range(N//2):
   x_sum += int(arr[x]) #idx개수만큼
for y in range(N-1, N//2 - 1, -1): #역순
    y_sum += int(arr[y]) #idx번호=> 개수만큼 # unsupported operand type(s) for +=: 'int' and 'str'

#print(x_sum, y_sum)
if x_sum == y_sum:
    print('LUCKY')
else :
    print('READY')

'----------------------------------------'
#블로그 풀이
#미친 풀이.. 굿
arr = list(input()) #이렇게 받아서
left = list(map(int, arr[0:N//2]))
right = list(map(int, arr[N//2:N]))

if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')