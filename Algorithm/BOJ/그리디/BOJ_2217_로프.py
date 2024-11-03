# 문제의 키포인트는 모든 로프를 사용할 필요가 없는 것 !! == 이게 함정이다.
# 전체 값을 일단 내림차순 정렬하고
# 일단 중요한 것은 맨 마지막 값은 해당 되지 않음
# 따라서 현재의 값 *(count)를 해준다 => 내 앞에 있었던 친구는 이미 나의 값을 넘기 때문에 고려X
# 횟수 N을 모두 해주는게 아니라 나와 아까의 값을 곱해줘야 개수가 맞다
# 근데 최대를 구해야하기 떄문에 완전탐색으로 모든 경우를 구해야 한다.!!
N = int(input())
arr = [int(input()) for _ in range(N)] #N만큼 list를 만들고
arr.sort(reverse=True) #내림차순으로 정렬한다
#count_num
max_weight = 0 #최대 중량을 구해야 함
#count = 1 #횟수를 카운트한다 => 1부터 시작해야함
#가장 큰 값은 무시하고 패스해야할까?
for i in range(N) : #역순으로 접근
    # if i == 0: #역순 => 그 반례케이스
    #     continue
    # count += 1 #곱할 N같은 x를 구하기 위함
    sum = arr[i] * (i+1) #현재의 값  => 최대 중량의 값 => 굳이 count를 할필요가 없을듯?
    #print(max_weight, sum)
    if sum >= max_weight:
        max_weight = sum #max_weight는 바뀌게 되는 것
    #맨 첫번째
print(max_weight)