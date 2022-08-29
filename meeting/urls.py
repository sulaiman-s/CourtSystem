from django.urls import  path
from .views import MeetingRequestView,MeetingRequestViewId,MeetingView,MeetingViewId
urlpatterns=[
    path('meetingRequest/',MeetingRequestView.as_view()),
    path('meetingRequestId/<int:id>',MeetingRequestViewId.as_view()),
    path('meetings/',MeetingView.as_view()),
    path('meetings/<int:id>',MeetingViewId.as_view())
]