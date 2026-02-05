from rest_framework.viewsets import ModelViewSet
from .serializer import Salom1Serializer,Salom2Serializer,Salom3Serializer,Salom4Serilaizer,Salom5Serializer
from .models import Salom5,Salom1,Salom2,Salom3,Salom4

class Salom1APIView(ModelViewSet):
    queryset=Salom1.objects.all()
    serializer_class=Salom1Serializer

class Salom2APIView(ModelViewSet):
    queryset=Salom2.objects.all()
    serializer_class=Salom2Serializer


class Salom3APIView(ModelViewSet):
    queryset=Salom3.objects.all()
    serializer_class=Salom3Serializer

class SalomAPI4View(ModelViewSet):
    queryset=Salom4.objects.all()
    serializer_class=Salom4Serilaizer


class Salom5APIView(ModelViewSet):
    queryset=Salom5.objects.all()
    serializer_class=Salom5Serializer