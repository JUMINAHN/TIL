# Django_Error log 7

날짜: 2024년 10월 12일

>> error 학습하고, 오류 메세지에 정답이 있음을 인지하자

# TypeError at / libraries / 1

---

- all() got an unexpected keyword argument 'pk'

![image.png](4524bf24-f1ae-49a7-8eb0-eb6049ba69bb.png)

→ index 페이지에서 detail쪽으로 가기 위한 경로의 과정에서 all()을 받아서 발생하는 듯 해보이는데,,

<aside>
💡

**1차 점검**

</aside>

[**index.html]** 

- list태그를 잘못 감싼 것을 확인 “ 음.. 무관
- 특정 태그의 author만 불러와서 pk를 접근했기 때문에 괜찮은 것 아닌가? →단순 pk로 받아서?
== 단순 pk가 맞다

```python
<body>
  <!--전체 목록을 확인할 수 있는 페이지 제공-->
  <h1>저자 전체 목록</h1>
  <!--authors를 보냇을 것-->
  <ul>
    {% for author in authors %}
      <!--author의 pk값을 기반으로 detail 페이지를 나타내기 떄문에-->
      <!--세부 내용으로 들어간다.-->
      <a href="{% url "libraries:detail" author.pk%}"><li>이름 : {{author.name}}</li></a> <!--상세 페이지-->
      <a href="{% url "libraries:detail" author.pk%}"><li>국적 : {{author.nationality}}</li></a>
      <hr>
    {% endfor %}
  </ul>
</body>
```

<aside>
💡

**2차 점검** 

</aside>

- all? → 이때까지 메인 페이지에 대한 내용을 보았다
    - 근데 실제적으로 link를 타고 들어가는 과정에서 detail의 오류가 있는 것을 다시 인지함

→ [views.py](http://views.py) 확인

```python
def detail(request, author_pk):
    #어디서? 게시글에 있는 디테일한 내용을 돌려받을 것입니다.
    author = Author.objects.all(pk=author_pk)#이 내용을 받을 것이고 -> 그걸 띄워줄 것입니다.
    context = {
        'author' : author
    } #detail 페이지에 돌려줄것입니다. == 일단은 
    #전반적인것 think
    return render(request, 'libraries/detail.html', context) #이걸 돌려줘야 함
```

- all로 표기되어 있는 것을 확인하고 → `get` 으로 수정

# 원하는 값이 출력되지 않음 → 전체 목록의 일부 data

---

![image.png](image.png)

[index.html]

```python
<body>
  <!--전체 목록을 확인할 수 있는 페이지 제공-->
  <h1>저자 전체 목록</h1>
  <!--authors를 보냇을 것-->
  <ul>
    {% for author in authors %}
      <!--author의 pk값을 기반으로 detail 페이지를 나타내기 떄문에-->
      <!--세부 내용으로 들어간다.-->
      <li><a href="{% url "libraries:detail" author.pk%}">이름 : {{author.name}}</a></li> <!--상세 페이지-->
      <li><a href="{% url "libraries:detail" author.pk%}">국적 : {{author.nationality}}</a></li>
      <!--author의 book-->
      <li><a href="{% url "libraries:detail" author.pk%}">집필 권 수 : {{author.book | length}}</a></li> <!--author를 기준으로 접근-->
      <hr>
    {% endfor %}
  </ul>
</body>
```

→ `html` 태그에서도 역참조를 사용할 수 있다.

<aside>
💡

**명심할 포인트**

</aside>

1. html 코드에서도 역참조로 접근할 수 있다
2. 1 : N관계에서 → N으로 1에 접근할 수 있다
ex) [comments.article.pk](http://comments.article.pk) 

# **AttributeError at /libraries/**

---

- 'QuerySet' object has no attribute 'book_set'

![image.png](image%201.png)

→ bookset 설정의 문제이다 : view 함수 확인

```python
def index(request) : #그냥 지금은 -> 저자 전체 목록 확인할 수 있는 페이지 구성
    #저자..
    #지금 유의할 점이있는데 -> author.pk의 인자를 index에서 받아야하는데 활용할 수 없다는 점..
    authors = Author.objects.all()
    #집필권수 -> author로 book의 정보를 출력해야 함 #역참조
    books = authors.book_set.all() #불러지지 않음
    context = {
        'authors' : authors,
        'books' : books
    }
    return render(request, 'libraries/index.html', context)

```

→ 현재 생각된 문제점은 book이라는 instance를 불러오지 못했기 떄문이라고 판단됨

<aside>
💡

수정 1 → BOOK() 선언 후 추가했으나 동일한 이슈

</aside>

```python
from .models import Author, Book
from .forms import BookForm

# Create your views here.
def index(request) : #그냥 지금은 -> 저자 전체 목록 확인할 수 있는 페이지 구성
    #저자..
    #지금 유의할 점이있는데 -> author.pk의 인자를 index에서 받아야하는데 활용할 수 없다는 점..
    authors = Author.objects.all()
    #집필권수 -> author로 book의 정보를 출력해야 함 #역참조
    #book = Book()
    books = authors.book_set.all() #불러지지 않음
    context = {
        'authors' : authors,
        'books' : books
    }
    return render(request, 'libraries/index.html', context)
```

<aside>
💡

문제 원인 파악 : book_set은 개별 인스턴스에서만 사용 가능

</aside>

- 코드가 작동하지 않는 이유는 **`authors`**가 **`QuerySet`**이기 때문
- **`book_set`**은 개별 **`Author`** 인스턴스에서만 사용 가능

# TypeError at /libraries/1/books/create

---

- books_create() got an unexpected keyword argument 'author_pk'

![image.png](image%202.png)

→ 예기치 못한 값을 받았다고 하고 있다.

[detail.html]

```python
  <form action="{% url "libraries:books_create" author.pk%}" method="POST"> <!--어디로 보낸다? : 댓글이니까 댓글 생성 페이지로-->
    {% csrf_token %}
    {{book_form.as_p}}
    <input type="submit" value="CREATE">
  </form>
```

[views.py]

```python
def books_create(request, article_pk): #airticle_pk에 대한 정보를 받는다
    #if로 구분할 필요가 없음 post로만 받으니까 -> 데이터를 post로 받아온다.
    #기존과 동일
    author = Author.objects.get(pk=article_pk)
    book_form = BookForm(request.POST) #requestPOST -> 이거에 대한 정보를 받았으니 유효성 검증이 진행되어야 함
    if book_form.is_valid():
        book = book_form.save(commit=False) #article에 대한 데이터를 보내줘야 함
        book.author = author #어떤 게시물에 관련된 것인지 받아야 하기 떄문임
        book_form.save()
        return redirect('libraries:detail')
    context = {
        'author' : author,
        'book_form' : book_form
    }
    return render(request, 'libraries/detail.html', context)
```

<aside>
💡

코드 수정 1

</aside>

```python
def books_create(request, article_pk): #airticle_pk에 대한 정보를 받는다
    #if로 구분할 필요가 없음 post로만 받으니까 -> 데이터를 post로 받아온다.
    #기존과 동일
    author = Author.objects.get(pk=article_pk)
    book_form = BookForm(request.POST) #requestPOST -> 이거에 대한 정보를 받았으니 유효성 검증이 진행되어야 함
    if book_form.is_valid():
        book = book_form.save(commit=False) #article에 대한 데이터를 보내줘야 함
        book.author = author #어떤 게시물에 관련된 것인지 받아야 하기 떄문임
        book_form.save()
        return redirect('libraries:detail', article_pk) #세부 데이터를 보여줘야하는데 그러한 인자가 없음 -> 여기에 이슈
    context = {
        'author' : author,
        'book_form' : book_form
    }
    return render(request, 'libraries/detail.html', context)

```

→ detail page를 보여줄때 어떤 게시글의 세부적인 내용을 보여줄 것인지에대한 매개 인자가 빠진듯하여
     redirect 부분을 수정함

<aside>
💡

코드 수정2 → 오타 

</aside>

- URL 패턴과 뷰 함수의 **매개변수가 일치하지 않아서 발생하는 이슈**
    - author_pk로 설정하고 계속 aritcle_pk로 받고 있음