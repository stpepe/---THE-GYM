# Generated by Django 4.0 on 2021-12-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phonenumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('secname', models.CharField(max_length=20)),
                ('dadname', models.CharField(max_length=20)),
                ('phonenumber', models.IntegerField(max_length=11)),
            ],
        ),
    ]
