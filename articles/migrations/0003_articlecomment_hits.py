# Generated by Django 3.2.13 on 2022-12-02 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20221201_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecomment',
            name='hits',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
    ]