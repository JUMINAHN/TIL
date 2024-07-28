hello = 1, 2, 3, 4, 5
print(hello) #tuple --> 여러가지를 봉지에 담음
#여러개를 줌

#한개를 배분해줌
a, b, c, d, e = hello
print(a,b,c,d,e)

# a,b,c = hello
# print(a,b,c) #unpack할게 더 많다

#list에서 *게 된다.
a, b, *c = hello
print(a)
print(b)
print(c)
#앞에 해야한다 #list화 된다.
print("-"*30)
number = [1,2,3,4,5]
a,b,*c = number
print(a)
print(b)
print(c)

#여러개 -> 비닐봉지(한 묶음)
#비닐봉지 -> 여러개 -> 개수가 안맞으면 걔는 장바구니를 들고 있는 것
