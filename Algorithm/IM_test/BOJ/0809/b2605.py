#번호를 0번부터 세우면 좋지 않을까? 근데 그러면 위치가 복잡해질 것 같다
#그래서 뒤에서부터 역순으로 [::-1]로 값을 읽어온다면 더 편하지 않을까?
#insert 내장 함수를 사용하면 풀 수 있을 것 같다.
#그리고 어짜피 뭐가되든 초기에 0번은 setting 되어있는 상태이다.
student_num = int(input())
student = list(map(int, input().split())) #0 1 1 3 2가 들어간다

line_number = [1] #1번 친구는 항상 0번 idx에 위치
for idx, one in enumerate(student): #idx가 0부터 시작하기 때문에
    if idx == 0:
        continue
    line_number.insert(one, idx+1) #어떤 위치에 어떠한 순번이 들어가는지
    result = line_number[::-1]
print(*result)