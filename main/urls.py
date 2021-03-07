from django.urls import path
from main import views

app_name = 'main' #指名此app名稱為main
urlpatterns = [
    path('', views.main, name='main'), #url是main/時做處理 
    path('about/', views.about, name='about'), #url是main/about/時做處理
]
#views.main->main.views模組裡面的mian方法
#將此url命名為main

#記得要去專案blog的url.py設定此app main 的path