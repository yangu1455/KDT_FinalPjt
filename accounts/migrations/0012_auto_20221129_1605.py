# Generated by Django 3.2.13 on 2022-11-29 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_merge_20221129_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default=1, max_length=254, verbose_name='email address'),
            preserve_default=False,
        ),
    ]