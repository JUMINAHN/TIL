N = int(input()) #시험장 개수
Ai = list(map(int, input().split())) #각 시험장에 있는 응시자의 수
B, C = map(int, input().split()) #총감독, 보조감독

count = 0
for A in Ai: #응시자 수 하나 하나씩 --> 총감독을 먼저뺴고 보조감독만 나중에 한꺼번에 계산하자
    A = A - B
    count += 1 #뺀 것 자체도
    if A == 0:
        count += 1
        break
    else :
        if A % C == 0:
            count += (A//C)
        else :
            if A % C <= C:
                count += 1
print(count)
