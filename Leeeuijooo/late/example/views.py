from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])

def helloAPI(request):
    return Response('전송될 데이터')
