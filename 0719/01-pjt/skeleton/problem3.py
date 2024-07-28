import requests
from pprint import pprint

# 문제3. B번에서 얻는 결과를 활용하여, KEY 값들을 한글로 변경한 딕셔너리를 반환하도록 구성합니다.
# KEY 에 해당하는 한글 KEY 값들은 다음과 같습니다.
def get_weather(api_key):
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    data = requests.get(url).json()
    results = data.keys() #key들만 담은 것

    new_dict = {}
    for result in results:
      if result == 'main' or result == 'weather': #논리식 오류 확인
        new_dict[result] = data[result] #data에 있는 값과 동일하게  
        
    

    another_dict = {} #자체를 복사할 것이 아니기 때문에
    inner_dict = {}
    #dictionary 내부 안의 내부 값 변경하자
    #dirty code
    inner_dict['기압'] = data['main']['pressure']
    inner_dict['습도'] = data['main']['humidity']
    inner_dict['온도'] = data['main']['temp']
    inner_dict['체감온도'] = data['main']['feels_like']
    inner_dict['최고온도'] = data['main']['temp_max']
    inner_dict['최저온도'] = data['main']['temp_min']
    another_dict['기본'] = inner_dict 

    sub_data = []
    sub_dict = {}
    sub_dict['식별자'] = data['weather'][0]['id']
    sub_dict['아이콘'] = data['weather'][0]['icon']
    sub_dict['요약'] = data['weather'][0]['description']
    sub_dict['핵심'] = data['weather'][0]['main']
    sub_data.append(sub_dict)
    another_dict['날씨'] = sub_data

    return another_dict


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # 여러분의 OpenWeatherMap API 키를 설정하세요
    api_key = '02632a1a19eafa7854c4b90c94158271'

    result = get_weather(api_key)
    pprint(result)
