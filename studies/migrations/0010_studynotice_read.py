# Generated by Django 3.2.13 on 2022-12-09 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0009_auto_20221209_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='studynotice',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]