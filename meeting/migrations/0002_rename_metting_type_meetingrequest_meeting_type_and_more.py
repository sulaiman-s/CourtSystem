# Generated by Django 4.0.5 on 2022-08-27 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetingrequest',
            old_name='metting_type',
            new_name='meeting_type',
        ),
        migrations.RenameField(
            model_name='meetings',
            old_name='metting_type',
            new_name='meeting_type',
        ),
    ]
