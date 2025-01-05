#우리 계단 문제보단 쉬운 것 같음
def upscale(num_list, num_length):
    #숫자들의 크기를 비교한다.
    #그리고 비교된 것을 max_num에 넣는다. -> idx 접근해야 해서 num_length를 이용하면 좋음
    max_length = 0
    count_num = 1 #길이가 0부터 시작하는게 아니라 1부터 시작
    for i in range(1, num_length): #왜냐면 앞 뒤를 비교할 것인데 0부터 시작하면 범위가
        #증가 조건 -> #클 경우
        if num_list[i] >= num_list[i-1]:
            count_num += 1
        else :
            count_num = 1
        #크기 비교 조건
        if max_length < count_num:
            max_length = count_num
    return max_length

def downscale(num_list, num_length):
    min_length = 0
    count_num = 1
    for i in range(1, num_length): #왜냐면 앞 뒤를 비교할 것인데 0부터 시작하면 범위가
        #증가 조건 -> #클 경우
        if num_list[i] <= num_list[i-1]: #마지막에 안도나..?
            count_num += 1
        else :
            count_num = 1 #다시 초기 값으로 맞춰 줘야함
        #크기 비교 조건
        if min_length < count_num:
            min_length = count_num
    return min_length

#총길이를 구한다.
num_length = int(input())
num_list = list(map(int, input().split()))

up = upscale(num_list, num_length)
down = downscale(num_list, num_length)
if up > down:
    print(up)
elif up < down:
    print(down)
else :
    print(up) #똑같으니까 아무거나해도 상관없음