from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ClientNotification, LawyerNotification, Notification
# Create your views here.


class notificationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'name', 'token')


class LawyerNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawyerNotification
        fields = ('id', 'lawyer_name', 'message')


class ClientNotificationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = ClientNotification
        fields = ('id', 'client_name', 'message')


class NotificationView(APIView):
    def get(self, request):
        gettokens = Notification.objects.all()
        se = notificationSerailizer(gettokens, many=True)
        return Response(se.data)

    def post(self, request):
        gettokens = Notification.objects.filter(
            name__contains=request.data['name'])
        if (len(gettokens) > 0):
            return Response('already exist')
        else:
            se = notificationSerailizer(data=request.data)
            se.is_valid(raise_exception=True)
            se.save()
        return Response('ok')


class LawyerNot(APIView):
    def get(self, request, name):
        lawyernot = LawyerNotification.objects.filter(
            lawyer_name__exact=name)
        se = LawyerNotificationSerializer(lawyernot, many=True)
        return Response(se.data)

    def post(self, request, name):
        se = LawyerNotificationSerializer(data=request.data)
        se.is_valid(raise_exception=True)
        se.save()
        return Response('ok')

    def delete(self, request, name):
        td = LawyerNotification.objects.get(pk=name)
        td.delete()
        return Response('deleted')


class ClientNot(APIView):
    def get(self, request, name):
        Clientnot = ClientNotification.objects.filter(
            client_name__contains=name)
        se = LawyerNotificationSerializer(Clientnot, many=True)
        return Response(se.data)

    def post(self, request, name):
        se = ClientNotificationSerailizer(data=request.data)
        se.is_valid(raise_exception=True)
        se.save()
        return Response('ok')

    def delete(self, request, name):
        td = ClientNotification.objects.get(pk=name)
        td.delete()
        return Response('deleted')
