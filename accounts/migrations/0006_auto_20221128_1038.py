# Generated by Django 3.2.13 on 2022-11-28 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='boj_id',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='github_id',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]