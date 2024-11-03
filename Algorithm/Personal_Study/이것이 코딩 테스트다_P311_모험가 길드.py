
# 이코테의 정답 풀이 == 이해가 안됨
# 공포도가 낮은 사람부터 처리하기 떄문에 많은 그룹을 만들 수 있따
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

group = 0
count = 0
for i in arr:
    #배열을 순회하면서 모험가를 하나씩 그룹에 포함
    count += 1
    #만약 현재 그룹에 포함된 모험가 수(count)가 해당 모험가의 공포도(i)보다 크거나 같으면,
    # 그룹을 결성할 수 있다.
    # 그러면 group을 하나 증가시키고, count를 다시 0으로 초기화
    if count >= i:
        group += 1
        count = 0
'-------------------------------------------'
# 지피티 참고 => 공포도가 높은 모험가 부터 처리한 경우
N = int(input())
arr = list(map(int, input().split()))

group = 0
arr.sort(reverse=True)  # 공포도가 높은 순서대로 정렬

count = 0  # 현재 그룹에 포함된 모험가의 수

for i in arr:
    count += 1  # 현재 그룹에 모험가를 포함
    if count >= i:  # 현재 그룹의 인원수가 해당 모험가의 공포도 이상이면 그룹 결성
        group += 1
        count = 0  # 새로운 그룹을 위해 초기화

print(group)

'--------------------------------------------'
# 나의 풀이

# 그룹수가 최대 몇개를 만들 수 있는가?
# 완전탐색으로 제일 큰 수를 고르면 될 것 같음
# 받은 input 개수 N에서 제일 큰 수 == X를 뺴주고
# N-x된 값 즉 N = N-x에 (x-1) 이걸 계속 줄여가면서 count += 1하면 되지 않을까?
'''
5
2 3 1 2 2
'''

N = int(input())
arr = list(map(int, input().split())) #2 3 1 2 2 인 상태
x = 0 #최대값을 넣을 친구
for a in arr:
    if x <= a:
        x = a #최대값을 게속 반영해주고
count = 0 #그 부분을 셀 변수
# 그값을 빼준다

#즉 0이될때까지가 아니라 음수가 되면 종료
#값이 증가될 것이기 떄문에
idx = 0
while N > 0 : #0이랑 같으면 => 계산할 필요가 없음
    N -= (x-idx) # 그럼 값이 남을 것 인데
    count += 1
    idx += 1 #idx도 증가시켜줄 것
    #print(N) #디버ㅇ깅을 위해서
#자 여기서 N -= (x-1)을 하고
#count += 1을 해줄 것
print(count) #count의 값 나타내기