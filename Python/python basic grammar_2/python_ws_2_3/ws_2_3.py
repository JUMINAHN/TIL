books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
authors = ['작자 미상', '허균', '박지원', '이항복', '임제']

print(f'{authors[1]} : {books[-2]}')
print(f'{authors[-2]} : {books[1]}')
print(f'{authors[0]} : {books[2]}')
print(f'{authors[2]} : {books[0]}')
print(f'{authors[-1]} : {books[-1]}') 

# result = {}
# result[authors[1]] = books[-2]
# result[authors[-2]] = books[1]
# result[authors[0]] = books[2]
# result[authors[2]] = books[0]
# result[authors[-1]] = books[-1]


#키 값만 출력됨
#print(result)
# for i in result:
#     print(i)