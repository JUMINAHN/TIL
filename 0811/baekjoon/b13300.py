import sys
sys.stdin = open("input1330.txt")

N, K = map(int, input().split())
student = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]} #리스트 안에 담기
for _ in range(N):
    S, Y = map(int, input().split())
    sth = student.get(Y) #key로 value값을 뽑아서 -> 리스트에 배열화
    sth.append(S)
print(student)

total = 0
for sk in student.keys(): #특정 키와 특정 벨류에 대한
    zero_count = 0
    one_count = 0
    #value 안에서 순회
    for v in student.get(sk) : #value 값들
        if v == 0:
            zero_count += 1
        else :
            one_count += 1 #이까지 맞게 담긴 것도 확인
    #조건을 명확하게 설정하자
    #지금처럼 짜면 2이상일 떄 들어가고
    gene_count = [zero_count, one_count]
    for gene in gene_count:
        if gene % K >= 1:
            total += 1
        total += gene // K #몫이 없으면 0이되겠지

print(total)