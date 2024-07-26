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
#앞에 해야한다
print("-"*30)
number = [1,2,3,4,5]
a,b,*c = number
print(a)
print(b)
print(c)
