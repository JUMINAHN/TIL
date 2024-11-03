import requests

URL = "MYURL" #?는 사용X? => 지금 xml파일로 받았었음
params = {
    'auth' : '', #인증키
    'topFinGrpNo' : '020000',
    'pageNo' : 1
}

#response = requests.get(url=URL, params=params).text => text 형태로
# response = requests.get(url=URL, params=params).json() #requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
response = requests.get(url=URL, params=params) #requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
json_data = response.json() #requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
#json_data = response.json() => file형식 오류로 출력이 되지 않았었음
#print(json_data) 


#정보들 추출 하기 
#print(json_data.get('result').get('base_List')) 

#상품목록 => 상품 => 기본정보 : 금융회사 명, 금융 상품명, 가입 방법, 만기 후 이자율 , 우대 조건, 가입 제한, 가입 대산, 최고 한도
#kor_co_nm	, fin_prdt_nm, join_way	, mtrt_int	,spcl_cnd	, join_deny	, join_member , max_limit	
product_info = []

for data in json_data.get('result').get('baseList'): #list 영역 한개씩 나올 것 => 'NoneType' object is not iterable => 오탈자
    kor_co_nm = data.get("kor_co_nm") 
    join_way = data.get("join_way") 
    mtrt_int = data.get("mtrt_int")
    spcl_cnd = data.get("spcl_cnd") 
    join_deny = data.get("join_deny") 
    join_member = data.get("join_member") 
    max_limit = data.get("max_limit")   

    save_data = {
        "kor_co_nm" : kor_co_nm, 
        "join_way" : join_way, 
        "mtrt_int": mtrt_int, 
        "spcl_cnd": spcl_cnd, 
        "join_deny": join_deny,
        "join_member": join_member, 
        "max_limit":max_limit,   
        }
    product_info.append(save_data)
print(product_info)

#상품목록 => 상품 => 옵션 정보 : 저축 금리 유형, 저축 기간, 저축 금리, 최고 우대 금리
#intr_rate_type, save_trm, intr_rate, intr_rate2	
product_option = []
for option in json_data.get('result').get('optionList'):
    intr_rate_type = option.get("intr_rate_type")
    intr_rate_type_nm = option.get("intr_rate_type_nm")
    save_trm = option.get("save_trm")
    intr_rate = option.get("intr_rate")
    intr_rate2 = option.get("intr_rate2")

    save_option = {
        "intr_rate_type" : intr_rate_type,
        "intr_rate_type_nm" : intr_rate_type_nm,
        "save_trm" : save_trm,
        "intr_rate" : intr_rate,
        "intr_rate2" : intr_rate2,
    }
    product_option.append(save_option)
print(save_option)
