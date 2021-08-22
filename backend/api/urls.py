# url 연결 (frontend와 통신)

from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from api import views
from . import views

router = DefaultRouter(trailing_slash=False)

urlpatterns = [

    path('user/join/', views.user_join),
    path('user/login/', views.user_login),
    path('user/info/', views.user_info),
    path('count/', views.count),
    path('myaccount/', views.myaccount),
    path('findaccount/', views.findaccount),
    path('oneaccount/', views.oneaccount),
    path('trade/', views.tradefinish),
    path('trade/add/', views.addtrade),
    path('week/', views.getweek),
    path('record/', views.record),
    path('adver/get/', views.getadver),
    path('adver/all/', views.alladver),
    path('record/tradefive/', views.tradefive),
    path('date/', views.date),
    path('record/list/', views.recordlist),
    path('account/add/', views.addaccount),
    path('account/change/', views.change),
    path('card/', views.card),
    
]