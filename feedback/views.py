from dataclasses import field
from django.shortcuts import render
from .models import FeedBack
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
# Create your views here.


class FeedbackSerialzer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ['id', 'username', 'lawyer_name', 'message', 'star_ratings']


class FeedbackView(APIView):
    def get(self, request):
        getAll = FeedBack.objects.all()
        se = FeedbackSerialzer(getAll, many=True)
        return Response(se.data)

    def post(self, request):
        se = FeedbackSerialzer(data=request.data)
        se.is_valid(raise_exception=True)
        se.save()
        return Response(se.data)
