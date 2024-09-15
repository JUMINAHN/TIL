#import sys
#sys.stdin = open('input2309.txt')

#일곱 난쟁이
#7명이 아니라 9명이 집으로 돌아왔다 -> 2명의 거짓말 쟁이 존재
#그런데 7명의 합이 100이 됨을 기억했다
#100빼기 남는 값을 구해라

small = [] #난쟁이들 시리즈로 담음
for _ in range(9):
    small.append(int(input()))
find = sum(small) - 100 #이제 두개의 합이 40인사람을 찾으면 된다.
#40인 사람을 small에서 빼주자

#조합?
check = []
for i in range(len(small)):
    for j in range(i+1, len(small)):
        total = small[i] + small[j] #둘이 겹치지 않겠지?
        if total == find : #40이라면
            check.append(small[i])
            check.append(small[j])

        #하지만 이 문제에서는 단 하나의 유효한 해답만 필요합니다
        #"가능한 정답이 여러 가지인 경우에는 아무거나 출력한다"
        #조건을 만족하는 첫 번째 쌍을 찾으면, 그것이 바로 우리가 찾는 가짜 난쟁이 두명 == 더 탐색 할 필요가 없음
        # 정확히 100이 됩니다.
        if check: #정확히 7명의 진짜 난쟁이를 찾아야 합니다.
            break
            #난쟁이가 아닌 후보친구들을 넣는다

small.sort()#오름차순 정렬
for s in small:
    if s in check:
        continue
    print(s)
