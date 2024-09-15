A = int(input()) #값을 전달받고
result = [] #리스트에 넣고
max = 0 #최대값을 0으로 기본 설정을 한다.
### 여기까지는 내가 생각한 부분과 동일하게 접근한다.
#내가 구현하고 싶었던 것 그대로 접근한 로직이다.

for i in range(A + 1): #1부터 100까지 -> 오 로직이 비슷하다.
    tmp = [A] #임시로 담은 것
    tmp.append(i)

    while (tmp[-2] - tmp[-1]) >= 0: #앞에 2개까지만 필요하니까 뒤에서부터 가지고 있는 두개를 접근하는 로직으로 시작한다.
        tmp.append(tmp[-2] - tmp[-1]) #그리고 그 결과값을 tmp에 담는다. --> 이러한 행위가 반복된다.

        if len(tmp) > max: #만약 이 길이가 가장 크다면?
            max = len(tmp) #맥스에 담고
            result = tmp #리저트에 담는다.

print(len(result))

for i in result:
    print(i, end=" ")