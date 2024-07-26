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

#보유하고 있지 않는 도서는 missing_book
#리스트 컴프리핸션을 사용하여 구현하기

all_book = True
missing_book = [rental for rental in rental_book if rental not in list_of_book]

# missing_book = []
# for rental in rental_book:
#     if rental not in list_of_book:
#         all_book = False
#         missing_book.append(rental)

if missing_book :
    for missing in missing_book:
        print(f'{missing} 을/를 보충하여 합니다.')
else : 
    print('모든 도서가 대여 가능한 상태입니다.')