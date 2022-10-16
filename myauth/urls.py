from django.urls import path
from django.contrib.auth import views as auth_views
from .views import MyTokenObtainPairView, LawyerView, LawyerId, UserView, Profiles, ProfilesSpec
urlpatterns = [
    path('create/', MyTokenObtainPairView.as_view()),
    path('lawyer/', LawyerView.as_view()),
    path('lawyer/<int:id>', LawyerId.as_view()),
    path('get/<str:name>',  UserView.as_view()),
    path('profile/', Profiles.as_view()),
    path('profile/uid/<str:id>', ProfilesSpec.as_view()),
    path('profile/<str:name>', ProfilesSpec.as_view()),
    path('password_reset/', auth_views.PasswordResetView.as_view(
         template_name='registration/common/password_reset_form.html'), name='password_reset_form'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView
         .as_view(template_name='registration/common/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/common/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/common/password_reset_complete.html'), name='password_reset_complete'),
]
