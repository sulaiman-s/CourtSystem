from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MeetingRequest, Meetings


# Create your views here.

class MeetingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRequest
        fields = ('id', 'client_name', 'lawyer_name', 'time', 'meeting_Status',
                  'meeting_type', 'meeting_Location', 'description')


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetings
        fields = ('id', 'client_name', 'lawyer_name', 'time',
                  'meeting_type', 'meeting_Location', 'description')


class MeetingRequestView(APIView):
    def get(self, request):
        all_meeting_request = MeetingRequest.objects.all()
        serialize = MeetingRequestSerializer(all_meeting_request, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = MeetingRequestSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response('posted')


class MeetingRequestViewId(APIView):
    def patch(self, request, id):
        mt_to_update = MeetingRequest.objects.get(pk=id)
        mt_s = MeetingRequestSerializer(
            mt_to_update, data=request.data, partial=True)
        mt_s.is_valid(raise_exception=True)
        mt_s.save()
        return Response(mt_s.data)

    def delete(self, request, id):
        mt_to_delete = MeetingRequest.objects.get(pk=id)
        mt_to_delete.delete()
        return Response("data deleted successfully")


class MeetingView(APIView):
    def get(self, request):
        all_meeting = Meetings.objects.all()
        serialize = MeetingSerializer(all_meeting, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = MeetingSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response('posted')


class MeetingViewId(APIView):
    def patch(self, request, id):
        mt_to_update = Meetings.objects.get(pk=id)
        mt_s = MeetingSerializer(mt_to_update, data=request.data, partial=True)
        mt_s.is_valid(raise_exception=True)
        mt_s.save()
        return Response(mt_s.data)

    def delete(self, request, id):
        mt_to_delete = Meetings.objects.get(pk=id)
        mt_to_delete.delete()
        return Response("data deleted successfully")
