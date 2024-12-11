data = [{'has_more': False,
  'next_cursor': None,
  'object': 'list',
  'page_or_database': {},
  'request_id': 'a5163fff-758f-45ea-b6fb',
  'results': [{'archived': False, #5번째 인덱스
               'cover': None,
               'created_by': {'object': 'user'},
               'created_time': '2023-06-15T04:29:00.000Z',
               'icon': None,
               'last_edited_by': {'object': 'user'},
               'last_edited_time': '2023-12-12T09:19:00.000Z',
               'object': 'page',
               'parent': {'type': 'database_id'},
               'properties': {'setNum': {'id': '%7DK%40%5C', #0번째 중 10번째 딕셔너리 요소
                                         'number': 1,
                                         'type': 'number'},
                              '과목': {'id': 'YuIE',
                                     'multi_select': [{'color': 'default',
                                                       'name': 'Python'}],
                                     'type': 'multi_select'},
                              '구분': {'id': '%40%3EmR',
                                     'select': {'color': 'purple',
                                                'name': '실습'},
                                     'type': 'select'},
                              '단계': {'id': 'T%7B%7BP',
                                     'select': {'color': 'default',
                                                'name': '3'},
                                     'type': 'select'},
                              '문제번호': {'id': 'uEBt',
                                       'number': 1431,
                                       'type': 'number'},
                              '제목': {'id': 'title', #5번째 -> 딕셔너리
                                     'title': [{'annotations': {'bold': False, #1번째 인덱스 -> 
                                                                'code': False,
                                                                'color': 'default',
                                                                'italic': False,
                                                                'strikethrough': False,
                                                                'underline': False},
                                                'href': None,
                                                'plain_text': '복잡한 자료구조',
                                                'text': {'content': '복잡한 자료구조',
                                                         'link': None},
                                                'type': 'text'}],
                                     'type': 'title'},
                              '일차': {'id': 'nWnH', #6번째
                                     'number': '2',
                                     'type': 'number'},
                              '커리큘럼': {'id': 'T%3AR_',
                                       'multi_select': [{'color': 'default',
                                                         'name': 'fundamentals-of-python'}],
                                       'type': 'multi_select'}},
               'public_url': None
            }],
  'type': 'page_or_database'}] #6번째 인덱스
#print(data[0]['results'][0]['properties']['제목']['title'][0]['plain_text'])
#print(data[0]['results'][0]['properties']['일차']['number'])
#print(data[0]['results'][0]['properties']['과목']['multi_select'][0]['name'])
#print(data[0]['results'][0]['properties']['단계']['select']['name'])

# 아래에 코드를 작성하시오.
first_data = {}
first_data['제목'] = data[0]['results'][0]['properties']['제목']['title'][0]['plain_text']
first_data['일차'] = data[0]['results'][0]['properties']['일차']['number']
value = data[0]['results'][0]['properties']['단계']['select']['name']
first_data['단계'] = f'{value}단계'
first_data['과목'] = data[0]['results'][0]['properties']['과목']['multi_select'][0]['name']
print(first_data)