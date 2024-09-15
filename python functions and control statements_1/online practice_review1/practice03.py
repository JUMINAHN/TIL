from conf import settings
from utils import create_url

NAME = settings.NAME
MAIN_URL = settings.MAIN_URL
result = create_url.create_url(NAME, MAIN_URL)
print(result)