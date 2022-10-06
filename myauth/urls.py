from django.urls import path
from .views import MyTokenObtainPairView, LawyerView, LawyerId, UserView, Profiles, ProfilesSpec
urlpatterns = [
    path('create/', MyTokenObtainPairView.as_view()),
    path('lawyer/', LawyerView.as_view()),
    path('lawyer/<int:id>', LawyerId.as_view()),
    path('get/<str:name>',  UserView.as_view()),
    path('profile/', Profiles.as_view()),
    path('profile/uid/<str:id>', ProfilesSpec.as_view()),
    path('profile/<str:name>', ProfilesSpec.as_view()),
]
