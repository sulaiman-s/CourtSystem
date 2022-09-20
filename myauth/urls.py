from django.urls import path
from .views import MyTokenObtainPairView, LawyerView, LawyerId, UserView
urlpatterns = [
    path('create/', MyTokenObtainPairView.as_view()),
    path('lawyer/', LawyerView.as_view()),
    path('lawyer/<int:id>', LawyerId.as_view()),
    path('get/<str:name>',  UserView.as_view())
]
