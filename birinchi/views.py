from .models import Salom1,Salom2,Salom3,Salom4,Salom5
from .serializer import Salom1Serializer,Salom3Serializer,Salom2Serializer,Salom4Serializer,Salom5Serializer
from rest_framework.generics import ListCreateAPIView

class Salom1APIView(ListCreateAPIView):
    serializer_class=Salom1Serializer
    queryset=Salom1.objects.all()

class Salom2APIView(ListCreateAPIView):
    queryset=Salom2.objects.all()
    serializer_class=Salom2Serializer

class Salom3APIView(ListCreateAPIView):
    queryset=Salom3.objects.all()
    serializer_class=Salom3Serializer

class Salom4APIView(ListCreateAPIView):
    queryset=Salom4.objects.all()
    serializer_class=Salom4Serializer


class Salom5APIView(ListCreateAPIView):
    queryset=Salom5.objects.all()
    serializer_class=Salom5Serializer