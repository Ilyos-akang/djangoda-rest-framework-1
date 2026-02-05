from django.urls import path,include
from rest_framework.routers import DefaultRouter
from  .import views

a=DefaultRouter()

a.register(r'salom1',views.Salom1APIView)
a.register(r'salom2',views.Salom2APIView)
a.register(r'salom3',views.Salom3APIView)
a.register(r'salom4',views.SalomAPI4View)
a.register(r'salom5',views.Salom5APIView)

urlpatterns=[
    path('',include(a.urls)),
]