from django.urls import path
from article import views

app_name = 'article' #指名此app名稱為article
urlpatterns = [
    path('', views.article, name='article'), #url是article/時做處理 
]
#views.article->article.views模組裡面的article方法
#將此url命名為article

#記得要去專案blog的url.py設定此app article 的path