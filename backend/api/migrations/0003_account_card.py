# Generated by Django 3.2.5 on 2021-08-22 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_advertising'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='card',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
