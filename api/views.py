from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GoldRateSerializer
from .models import GoldRate

# Create your views here.
class Grate(APIView):
    def get(self,request):
        goldrate = GoldRate.objects.all()
        ser = GoldRateSerializer(goldrate,many=True)
        return Response(ser.data)


