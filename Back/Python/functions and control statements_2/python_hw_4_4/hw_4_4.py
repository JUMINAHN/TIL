list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]


missing_book = [rental for rental in rental_book if rental not in list_of_book]
if missing_book: 
    for missing in missing_book:
        print(f'{missing} 을/를 보충하여야 합니다.')
else :
    print('모든 도서가 대여 가능한 상태입니다.')

# rental_book  = [
#     '장화홍련전',
#     '가락국 신화',
#     '온달 설화',
#     '금오신화',
#     '이생규장전',
#     '만복자서포기',
#     '수성지',
#     '백호집',
#     '원생몽유록',
#     '홍길동전',
#     '장생전',
#     '도문대작',
#     '옥루몽',
#     '옥련몽',
# ]



#보유하고 있지 않은 도서 따로 빼기
#리스트 컴프리핸션으로 만들기



#해당 부분은 일반 함수 
# missing_book = []
# for rental in rental_book:
#     if rental not in list_of_book:
#         print(f'{rental} 을/를 보충하여야 합니다.') #이거랑
#         missing_book.append(rental)


# if missing_book:
#         pass
# else :
#     print('모든 도서가 대여 가능한 상태입니다.')




