import imp
from django.urls import path
from .views import ClientView, ClientViewId, ClientViewName
urlpatterns = [
    path('lawyerClient/<str:name>', ClientViewName.as_view()),
    path('clients/', ClientView.as_view()),
    path('deleteClient/<int:id>', ClientViewId.as_view())
]
