# Generated by Django 4.0 on 2021-12-12 23:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_remove_phonenumbers_dadname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumbers',
            name='name',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(code='Invalid', message='Error', regex='\\d')], verbose_name='name'),
        ),
    ]
