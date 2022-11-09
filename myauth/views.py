from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import Lawyer, User, ProfilePic

# Create your views here.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password',
                  'email', 'location', 'gender', 'ph_no']


class UserView(APIView):
    def get(self, request, name):
        getUsers = User.objects.get(username=name)
        seri = UserSerializer(getUsers)
        return Response(seri.data)


class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = ['id', 'username', 'password', 'email', 'location',
                  'gender', 'doc_image', 'is_registered', 'ph_no', 'type', 'fullname']


class LawyerView(APIView):
    def get(self, request):
        get_all_lawyers = Lawyer.objects.all()
        serialize = LawyerSerializer(get_all_lawyers, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = LawyerSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        check_in_registered_user = User.objects.filter(
            username__exact=request.data['username'])
        if check_in_registered_user.count() > 0:
            return Response("user with this user already exist")
        serialize.save()
        return Response("Data save successfuly")


class LawyerId(APIView):
    def patch(self, request, id):
        lw_to_update = Lawyer.objects.get(pk=id)
        pf_s = LawyerSerializer(lw_to_update, data=request.data, partial=True)
        pf_s.is_valid(raise_exception=True)
        pf_s.save()
        return Response(pf_s.data)

    def delete(self, request, id):
        lw_to_delete = Lawyer.objects.get(pk=id)
        lw_to_delete.delete()
        return Response("data deleted successfully")


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.username
        token['email'] = user.email
        token['location'] = user.location
        token['is_active'] = user.is_active
        token['gender'] = user.gender
        token["is_admin"] = user.is_staff
        token["is_superuser"] = user.is_superuser
        token['ph_no'] = user.ph_no

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePic
        fields = ['id', 'name', 'profile_img']


class Profiles(APIView):
    def get(self, request):
        pf = ProfilePic.objects.all()
        pf_s = ProfileSerializer(pf, many=True)
        return Response(pf_s.data)

    def post(self, request):
        pf = ProfileSerializer(data=request.data)
        pf.is_valid(raise_exception=True)
        pf.save()
        return Response(pf.data)


class ProfilesSpec(APIView):
    def get(self, request, name):
        pf = ProfilePic.objects.filter(name__exact=name).first()
        pf_s = ProfileSerializer(pf)
        return Response(pf_s.data)

    def patch(self, request, id):
        pf_to_update = ProfilePic.objects.get(pk=id)
        pf_s = ProfileSerializer(pf_to_update, data=request.data, partial=True)
        pf_s.is_valid(raise_exception=True)
        pf_s.save()
        return Response(pf_s.data)

    def delete(self, request, id):
        pf_d = ProfilePic.objects.get(pk=id)
        pf_d.delete()
        return Response('deleted successfully')
