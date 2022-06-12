from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Lawyer
from django.utils.html import format_html


# Register your models here.
@admin.register(User,)
class UserAdmin(admin.ModelAdmin):
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             "classes": ("wide",),
    #             "fields": ("username", "password1", "password2", "location"),
    #         },
    #     ),
    # )
    list_display = ['username', 'location', 'is_staff', 'gender']


@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ['username', 'password','email', 'location', 'gender', 'doc_image','is_registered']

    # def image(self, obj):
    #     return format_html('<img src="{}" style="width: 100px; height:100px;" />'.format(obj.doc_image.url))
    #
    # image.allow_tags = True
