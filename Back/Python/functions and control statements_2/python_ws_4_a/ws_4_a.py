# 아래에 코드를 작성하시오.
from conf import settings
from utils import create_url

NAME = settings.NAME
MAIN_URL = settings.MAIN_URL

result = create_url.create_url(NAME, MAIN_URL)
print(result)
#모듈 객체를 함수처럼 = 'module' object is not callable
