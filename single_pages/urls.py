# urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('drug_detail/', views.drug_detail_view, name='drug_detail'),
]