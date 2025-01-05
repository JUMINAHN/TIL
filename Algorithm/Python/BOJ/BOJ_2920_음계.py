#다장조 == 8개의 음으로 구성
#1부터 8까지 차례대로 연주할 시 == ascending
#8부터 1까지 차례대로 연주할 시 == descending
#둘다 아니라면 == mixed

#for문으로 모두 증가시켰을 경우
#단순 무식한 방법 == 가끔은 이게 유용할 수 있음
asc = '1 2 3 4 5 6 7 8'
desc = asc[::-1] #reverse한 내용
#print(desc) == reverse 결과 확인함

data = input() #input == data를 받음
if data == asc :
    print('ascending')
elif data == desc :
    print('descending')
else :
    print('mixed')
