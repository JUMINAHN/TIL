
# Django 프로젝트 README

## 프로젝트 개요
이 프로젝트는 Django를 사용한 간단한 SNS 서비스입니다. 사용자는 게시글을 작성하고, 이미지를 업로드할 수 있습니다.

## 주요 기능
- 게시글 목록 조회 (index)
- 게시글 작성 (create)
- 게시글 상세 조회 (detail)

## 트러블슈팅

### 1. Static 파일 로딩 문제
**문제**: 템플릿에서 static 파일(이미지)이 로드되지 않음
**해결**: 
- static 태그를 올바르게 사용
  ```html
  <img src="{% static 'articles/2cat.jpg' %}" alt="2cat">
- static 파일의 경로를 정확히 지정
#
## 2. DB 마이그레이션 오류
문제: "no such column: articles_article.content" 오류 발생
해결: python manage.py migrate 명령어로 마이그레이션 실행

### 3. create 뷰 렌더링 오류
문제: create 화면이 index 화면과 동일하게 표시됨
해결: views.py에서 create 함수의 render 부분을 수정
python
return render(request, 'articles/create.html', context)

### 4. 폼 제출 버튼 동작 안함
문제: create.html의 폼 제출 버튼이 작동하지 않음
해결: <input type="button"> 을 <input type="submit">으로 변경

### 5. 미디어 파일 URL 설정 오류
문제: detail 페이지에서 이미지가 표시되지 않음
해결: urls.py의 static 설정을 수정
```python
urlpatterns = [
    # ... 기존 URL 패턴들 ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
주요 코드 스니펫
```python
views.py
python
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)
```
```python
urls.py
python
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
]
```

```html
create.html
xml
<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {{form.as_p}}
  <input type="submit" value="CREATE">
</form>
```

## 학습 내용
- Django의 MTV (Model-Template-View) 패턴
- 정적 파일 (Static files) 관리
- 폼 (Forms) 처리
- 미디어 파일 업로드 및 표시
- URL 설정 및 라우팅
- 향후 개선사항
- 사용자 인증 기능 추가
- 댓글 기능 구현
- 페이지네이션 적용