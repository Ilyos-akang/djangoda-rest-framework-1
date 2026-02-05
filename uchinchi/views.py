from .models import Salom5,Salom1,Salom2,Salom3,Salom4
from .serializer import Salom2Serializer,Salom1Serializer,Salom3Serializer,Salom4Serializer,Salom5Serializer
from rest_framework.viewsets import ModelViewSet


class Salom1APIView(ModelViewSet):
    queryset=Salom1.objects.all()
    serializer_class=Salom1Serializer

class Salom2APIView(ModelViewSet):
    queryset=Salom2.objects.all()
    serializer_class=Salom2Serializer

class Salom3APIView(ModelViewSet):
    queryset=Salom3.objects.all()
    serializer_class=Salom3Serializer

class SALOm4APIView(ModelViewSet):
    queryset=Salom4.objects.all()
    serializer_class=Salom4Serializer


class Salom5APIView(ModelViewSet):
    queryset=Salom5.objects.all()
    serializer_class=Salom5Serializer
