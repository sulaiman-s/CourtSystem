# Generated by Django 4.0.5 on 2022-06-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0006_alter_lawyer_doc_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyer',
            name='gender',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
