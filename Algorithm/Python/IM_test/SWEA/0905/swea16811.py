import sys
#43분 아이디어
sys.stdin = open('input16811.txt')

#입력
#T 수확횟수
# Testcase 수
T = int(input())
# Testcase 만큼 반복 #4시 56분~5시 11분, 14분~
for tc in range(1, T+1):
    # N 당근개수
    N = int(input())
    #출력값을 봤을 때 당근이 짝수인지 아닌지의 여부가 중요함
    #C 당근의 개수 N개만큼
    box = list(map(int, input().split())) #당근 방스

    #0.먼저 input을 받는 내용 정렬하기
    box.sort() #당근 뽑은 것 정렬하기
    #조건을 정리하다보니까 카운트 정렬이 핵심인 느낌 --> 누적
    #1<=Ci<=30 -> 당근을 담을 수 있는 최소 count 개수
    count = [0] * 31 #총 30개까지 담을 수 있고 0번 idx는 사용하지 않을 것임
    #1. 조건 구분 하기
        #1-1. count를 세서 가장 많이 세워진 것 => N // 2의 범위 초과하는 지 확인 : 50%를 초과하는 가?
    for b in box:
        count[b] +=1
    #대/중/소 박스 만들기 -> 미리 박스 크기 지정하자  (1-2조건에서 추가로 파생된 것)
    # count 정렬한 것으로 묶은 내용을 3등분해서 묶음으로 나누어 담으면 되지 않을까?
    # 그럼 누적 counting을 하는 것이 좋을 것 같은데..
    # 일단 위에서 50%가 넘지 않은 경우만 해당 되고 있으니 해당 부분은 고려하지 않아도 될 것 간긴하다..
    # 누적 counting을 해야할 것 같은데 --> 그걸 3등분 해야할 것 같은데
    # 그게 아니라면 count들 idx하면서 직접 누적해주고 --> 3번 나눠주기 ..?
    if N % 2 == 1 :
        big = [0] * (N//3) #대
        middle = [0] * (N//3) #중
        small = [0] * (N//3) #소
    else : #짝수라면?
        big = [0] * ((N//3))#대
        middle = [0] * ((N//3)+1) #중
        small = [0] * ((N//3)+1) #소

    #박스의 범위를 초과할 떄 담을 상자 -> 이게 있으면 result == -1이 되는 것
    trash = []

    #count의 크기가 N//2를 초과하는가?
    #count를 돌때 초과하는 가?
    result = 0
    check = 0
    #1-1의 조건인데 이걸 하면 나머지 2의 조건을 할 필요가 없음
    if result == 0: #일단 result가 0일때
        # 생각해보니까 상기 조건에 해당되면 -> 그 다음 조건을 해야하니 내부 if를 사용해야 한다.
        #if check != N: #check가 0이라는 것은 아직까지 아무런것도 할당을 하지 않았다는 뜻 -> 체크 변수말고
        # 1-2. 같은 크기인 것 같은 대/중/소 상자에 할당
        # 1-2-1. 같은 크기인 것을 어떻게 구분하는가?
            #범위를 초과한다면? 하지 않는다면?
            #그니까 범위가 초과하면 나가지는 것이지
        # 1-3. 각 상자에 든 당근 개수 차이가 최소가 되도록 포장 == count범위만큼 33.3%하기
        # 1-3-1. 상자의 범위가 중요한것보다는 누적합,,?이 중요할 것 같기도 한 문제 누적합과 idx를 사용하면 좋을 것 같은 생각/..?

        #변수 할당을 잘못하고 있는 듯 합니다. -> loop조건이 이상한 것 같음 아닌데 맞게 하고 있는데
        for c in count: # 1 1 1 1 1 1 이 들어가고 있음
                if 0 in small : #small에 0을 포함하고 있다면
                    for i in range(N//3):
                        small[i] = c #small에 c를 넣어주고
                elif 0 in middle :
                    for i in range(N//3):
                        middle[i] = c #m에 c를 넣어주고
                elif 0 in big :
                    for i in range(N//3):
                        big[i] = c #m에 c를 넣어주고
                else : #그게 아니면 큰 것에 할당을 해줘
                    trash.append(c)
        #print(trash)
        if 0 not in trash : #trash에 값이 있다면
            result = -1 #-1을 할당하고
        #not in 0

        print(small)
        print(middle)
        print(big)
        for c in count:
            if c > N//2: #50%를 넘어갈 때 문제가 됨
                result = -1 #포장할 수 없습니다. -> 대/중/소 상자까지 갈 필요가 없다.
                break
                # 아니면 그냥 break 하기 조건을 더 볼 필요도 없다. # 위치를 바꿔봄 --> 이중 조건이 성립되어서 어느정도 맞춤

    # print(len(big))
    # print(len(small))
    # print(len(middle))
    if result == -1:
        print(f'#{tc} {result}')
    else: #최대 최소
        max_num = max(len(big), len(middle), len(small))
        min_num = min(len(big), len(middle), len(small))
        print(f'#{tc} {max_num - min_num}')




    #출력
    #1. 당근이 포장되어있지 않으면 -1
    #2. 당근이 포장되어있으면 최소 차이값 출력