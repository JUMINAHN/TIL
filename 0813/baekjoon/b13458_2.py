N = int(input()) #시험장의 개수
Ai = list(map(int, input().split())) #각 시험장의 응시자의 수 --> loop를 돌 것
B, C = map(int, input().split()) #주감독관 보조감독관

count = 0 #감독관 수
#각 시험장의 응시자수를 뽑아야함 -> 1개씩 대응할 것
for num in Ai:
    num = num - B #전체인원에서 주감독관
    count += 1

    if num == 0: #주감독관으로 만족되면 끝
        continue #그게 아니면 다음 loop

    else: #그게 아니라면? 보조감독관을 구해야함
        #무조건적으로 나누는게 아니라 0으로 떨어지는 영역과 아닌 영역을 나눠야 할 것 같음
        if num % C == 0: # 다나눠 떨어지면
            count += num // C  # 나눠진 개수만큼 들어갈 것 -- 계속 대입을 해버렸다.. --> 왜 카운트를나눔? -> 그리고 나눠지기 전에 넣어야함
            num = num % C #0이겠지
            continue  # 그게 아니면 다음 loop

        else: #그게 아니라면 잔여가 있는 거면 즉 잔여가 그럼 C보다 작은 개수라면
            count += num // C #나눠지기 전에 넣어야함 --> 순서 로직 따라가기
            num = num % C
            if num < C: #이런 상황에서 잔여가 있다면
                count += 1

print(count)