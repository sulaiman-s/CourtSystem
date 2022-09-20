from django.urls import path
from .views import ClientNot, LawyerNot, NotificationView

urlpatterns = [
    path('notify/', NotificationView.as_view()),
    path('lawyernot/<name>', LawyerNot.as_view()),
    path('clientnot/<name>', ClientNot.as_view()),
]
