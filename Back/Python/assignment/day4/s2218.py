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

#대여 예정 -> 있는지 없는지 확인
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
    





# list_of_book = [
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

# rental_book = [
#     '장생전',
#     '위대한 개츠비',
#     '원생몽유록',
#     '이생규장전',
#     '데미안',
#     '장화홍련전',
#     '수성지',
#     '백호집',
#     '난중일기',
#     '홍길동전',
#     '만복자서포기',
# ]