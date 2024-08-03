#일단 data값이 주어졌을 떄 해당 내용을 counting 정렬하자
#예제에서 주어진 0,4,1,3,1,2,4,1 활용
data = [0,4,1,3,1,2,4,1]
N = len(data)
count = [0] * 5 #0부터 4까지 사용 -> 총 5
temp = [0] * N

#기본적으로 data, count, temp 세팅

#1. 각 개수를 센다 count -> data에 접근해서 data를 기반으로 idx를 살핀다.
for d in data:
    count[d] += 1 #해당 위치 idx에 해당 되는 값을 매칭시켜 증가시킨다.

#2. 각 개수를 누적시킨다. 0번인덱스는 건들지 않아도 된다. 누적될 값이 없기 떄문에
#따라서 인덱스 누적을 확인해야하기 떄문에 idx로 직접 접근한다.
for i in range(1, len(count)):
    count[i] = count[i-1] + count[i] #count i에 누적을 더한다. 이전값을

#3. 개수 누적을 기반으로 새로운 temp값에 해당되는 값을 매칭시킨다.
#뒤에서 부터 접근하며, 해당 값이 확인될경우 count를 감소시키고, 감소시킨 idx를 기반으로 temp idx를 매칭한다.
for i in range(N-1, -1, -1): #99번부터 0번 인덱스까지
    #i를 기반으로 data와 count에 모두 접근해야 한다. -> data를 기반으로 count를 찾고 감소시키자
    count[data[i]] -= 1
    idx = count[data[i]]
    temp[idx] = data[i] #내가 찾은 값을 매칭시킨다.

print(temp) #정렬된 배열 temp -> list화
print(*temp) #언패킹한다. --> 리스트에서 하나씩 꺼내진다.