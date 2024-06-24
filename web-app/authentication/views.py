from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        print("REQUEST",request.data)
        return Response(status=status.HTTP_200_OK)