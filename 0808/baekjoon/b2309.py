#일곱 난쟁의 합이 100
#100을 넘지 않는 자연수 아홉 난쟁이의 키는 모두 다르다
#가능한 정답이 여러가지인 경우 아무거나
import sys

sys.stdin = open('input2309.txt')
nanjeng2 = []
for i in range(9):
    nanjeng2.append(int(input()))

sum = 0
result = []
for nanjeng in nanjeng2:
    sum += nanjeng #모든 난쟁이의 키를 찾는다
    result.append(nanjeng)
#print(result)

total = sum - 100
s1, s2 = 0,0
for bignan in nanjeng2:
    for smallnan in nanjeng2:
        if total == (bignan + smallnan):
            s1 = bignan
            s2 = smallnan
            result.remove(bignan)
            result.remove(smallnan)
#선택정렬
for i in range(len(nanjeng2)-1):
    mid_idx = i
    for j in range(1+i, len(nanjeng2)):
        if nanjeng2[mid_idx] > nanjeng2[j]:
            mid_idx = j
    nanjeng2[i], nanjeng2[mid_idx] = nanjeng2[mid_idx], nanjeng2[i]

for nan in nanjeng2:
    if nan == s1 or nan == s2:
        continue
    print(nan)