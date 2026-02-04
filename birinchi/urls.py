from .views import Salom1APIView , Salom2APIView, Salom3APIView,Salom4APIView,Salom5APIView
from django.urls import path
urlpatterns=[
    path('salom1/',Salom1APIView.as_view()),
    path('salom2/',Salom2APIView.as_view()),
    path('salom3/',Salom3APIView.as_view()),
    path('salom4/',Salom4APIView.as_view()),
    path('salom5/',Salom5APIView.as_view()),

]