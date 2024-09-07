#모든 경우의 수 -> 반복문 안의 반복문
a = int(input()) #a = 2
for i in range(a): #i에 들어갈 수 있는 값 0과 1
    for j in range(a): #j값에도 0과 1
        print(i, j)
        # 0 0
        # 0 1
        # 1 0
        # 1 1