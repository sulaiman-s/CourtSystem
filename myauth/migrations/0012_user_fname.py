# Generated by Django 4.0.5 on 2023-02-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0011_lawyer_fullname_user_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fname',
            field=models.CharField(default='', max_length=255),
        ),
    ]
