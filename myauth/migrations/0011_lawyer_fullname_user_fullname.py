# Generated by Django 4.0.5 on 2022-11-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0010_profilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='fullname',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(default='none', max_length=255),
        ),
    ]
