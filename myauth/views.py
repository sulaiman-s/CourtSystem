from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework import  serializers
from rest_framework.response import Response
from .models import Lawyer

# Create your views here.

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lawyer
        fields=['id','username','password','email','location','gender','doc_image','is_registered']

class LawyerView(APIView):
    def get(self,request):
        get_all_lawyers=Lawyer.objects.all()
        serialize=LawyerSerializer(get_all_lawyers,many=True)
        return Response(serialize.data)
    def post(self,request):
        serialize=LawyerSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response("data sent successfuly")


class LawyerId(APIView):
    def patch(self,request,id):
        lw_to_update = Lawyer.objects.get(pk=id)
        pf_s = LawyerSerializer(lw_to_update, data=request.data, partial=True)
        pf_s.is_valid(raise_exception=True)
        pf_s.save()
        return Response(pf_s.data)
    def delete(self,request,id):
        lw_to_delete=Lawyer.objects.get(pk=id)
        lw_to_delete.delete()
        return  Response("data deleted successfully")


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.username
        token['email'] = user.email
        token['location']=user.location
        token['is_active']=user.is_active
        token['gender']=user.gender
        token["is_admin"] = user.is_staff
        token["is_superuser"]=user.is_superuser

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
