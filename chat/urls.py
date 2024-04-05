from django.urls import path
from chat import views

urlpatterns = [
    path('', views.main, name='main'),
    path('anon-chat/<str:room_name>/<str:nickname>', views.chat, name='main'),
]
