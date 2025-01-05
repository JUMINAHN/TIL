# 배열의 크기 N, 숫자가 더해지는 횟수 M, K(초과할 수 없음) -> 특정한 인덱스가 연속해서 세번까지만 더해질 수 있음
# N개의 자연수가 주어진다.
'''
5 8 3
2 4 5 4 6
'''

'''
#K는 항상 M보다 작거나 같다
#N, M, K = map(int, input().split()) #5 8 3
#N의 배열이 주어진다.
data = list(map(int, input().split())) #2 4 5 4 6
#예상 출력값 46
#가장 큰 값 ==> 666 5 666 5 => 36 + 10
#그러면 일단 가장 큰 값을 구하기 위해서 정렬해준다.
data.sort() #가장 data[-1]인 값이 젤 클 것

#일단 생각한 코드 끄적여본다.
num = 0 #더할 전체 값
total = 0
mx = 0
#M이 큰 경우 비효율적일 수 있음 -> 매번 조건을 확인하는 방식으로 비효율적일 수 있음
while M != total : #같아지면 나와질 것 => 3번 더해지는 방법 생각..
    if mx < K : #6이 한번 더 들어감
        num += data[-1]
        mx += 1
    else :
        num += data[-2]
        mx = 0
    total += 1
    #print(num)
print(num) #47이 나옴 -> 1이 더 많은데..
'''

'-------------------------------------'

#단순하게 푸는 문제로
N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
#활용할 반복 적인 요소 -> 변수 설정
first = data[-1]
second = data[-2]

result = 0 #값을 담을 결과 값
count = 0 #개수를 더할 것
while True: #M번쨰이면 종료
    for i in range(K): #연속적으로 더할 값
        if M == count:
            break
        count += 1
        result += first
    #그리고 second를 더할 것
    if M == count:
        break
    result += second
    count += 1
print(result)


''' ------------------------------------------ '''

#새로운 방식
N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
#활용할 반복 적인 요소 -> 변수 설정
first = data[-1]
second = data[-2]

count = int(M / (K+1)) * K
count += M % (K+1) #나머지 있을 경우
result = 0
result += (count) * first
result += (M-count) * second
print(result)