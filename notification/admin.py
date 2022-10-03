from django.contrib import admin
from .models import ClientNotification, LawyerNotification, Notification
# Register your models here.


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'token']


@admin.register(ClientNotification)
class CNotify(admin.ModelAdmin):
    list_display = ['client_name',
                    'message']


@admin.register(LawyerNotification)
class LNotify(admin.ModelAdmin):
    list_display = ['lawyer_name',
                    'message']
