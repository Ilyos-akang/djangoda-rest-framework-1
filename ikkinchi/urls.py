from .views import Salom1APIVIew,Salom2APIView,Salom4APIView,Salom3APIVew,Salom5APIView
from django.urls import path

urlpatterns=[
    path('salom1/',Salom1APIVIew.as_view()),
    path('salom2/',Salom2APIView.as_view()),
    path('salom3/',Salom3APIVew.as_view()),
    path('salom4/',Salom4APIView.as_view()),
    path('salom5/',Salom5APIView.as_view()),
]