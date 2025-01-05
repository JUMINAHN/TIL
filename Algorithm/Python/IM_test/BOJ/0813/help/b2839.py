N = int(input())

count = 0
while N >= 0: #0이고 음수이면 안되니까
    if N % 5 == 0: #5로 나누어 떨어진다면!
        count += N // 5 #5로 나누고
        print(count)
        break
    N -= 3 #5로 나누어 떨어지지 않는다면 3kg봉지 하나 사용
    count += 1
else :
    print(-1)