from rest_framework.routers import DefaultRouter
from .import views
from django.urls import path , include

r=DefaultRouter()
r.register(r'salom1',views.Salom1APIView)
r.register(r'salom2',views.Salom2APIView)
r.register(r'salom3',views.Salom3APIView)
r.register(r'salom4',views.SALOm4APIView)
r.register(r'salom5',views.Salom5APIView)


urlpatterns=[
    path('',include(r.urls)),
]