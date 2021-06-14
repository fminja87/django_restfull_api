from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import PhoneModelClass
from .serializers import PhoneModelSerializer


# Create your views here.


class Phones(APIView):
    def get(self, request):
        phones = PhoneModelClass.objects.all()
        serializer = PhoneModelSerializer(phones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serilizer = PhoneModelSerializer(data=request.data)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


def phone_object(id):
    try:
        phone = PhoneModelClass.objects.get(id=id)
        return phone
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


class PhoneDetails(APIView):

    def get(self, request, id):
        phone = phone_object(id)
        serializer = PhoneModelSerializer(phone)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        phone = phone_object(id)
        serializer = PhoneModelSerializer(phone, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        phone = phone_object(id)
        phone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
