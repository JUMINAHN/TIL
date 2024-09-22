#A*B*C를 계산한 결과부터 0부터 9까지의 숫자가 각각 몇번씩 쓰였는지 구해라
#A*B*C한 결과값에 대한 count
A = int(input())
B = int(input())
C = int(input())
multiply = str(A * B * C) #str으로 변환한 이유는 각 숫자가 어디에 해당되는지 확인하기 위함
count = [0] * 10 #0부터 9까지 -> 총 10개
for m in multiply:
   count[int(m)] += 1 #int로 변환

#print(count)
#해당 값 출력
for c in count:
    print(c)

