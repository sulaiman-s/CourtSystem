from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import Client
# Create your views here.


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'lawyer_name']


class ClientView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serialize = ClientSerializer(clients, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = ClientSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response("data sent successfuly")


class ClientViewName(APIView):
    def get(self, request, name):
        getclient = Client.objects.filter(lawyer_name__contains=name)
        se = ClientSerializer(getclient, many=True)
        return Response(se.data)


class ClientViewId(APIView):
    def delete(self, request, id):
        getc = Client.objects.get(pk=id)
        getc.delete()
        return Response('deleted')
