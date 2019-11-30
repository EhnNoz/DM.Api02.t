
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
# Create your views here.
@api_view(["POST"])
def EzafeKar(Working_Hour):
    try:
        Hour=json.loads(Working_Hour.body)
        ezafekar=str(Hour*15000)
        return JsonResponse("ezafekar = "+ezafekar+" $",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)


def EzafeKar2(Working_Hour2):
    try:
        Hour2=json.loads(Working_Hour2.body)
        ezafekar2=str(Hour2*15000)
        return JsonResponse("ezafekar = "+ezafekar2+" $",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)