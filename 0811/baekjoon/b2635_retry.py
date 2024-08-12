N = int(input())
total = []
max_length = 0

for i in range(1, N):
    temp = [N]
    temp.append(i)
    while 0 < temp[-2] - temp[-1]:
        result = temp[-2] - temp[-1]
        temp.append(result)

        if max_length < len(temp):
            max_length = len(temp)
            total = temp
            #total.append(temp)
print(max_length)
for t in total:
    print(t, end = " ")