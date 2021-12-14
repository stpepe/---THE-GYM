from django.db import models
from django.core.validators import *

# Create your models here.
class Phonenumbers(models.Model):
    name = models.CharField( ("name"), max_length=15, null=False, validators=[
        RegexValidator(
            regex=r'[A-ZА-Я]{1}[a-zа-я]{1,14}$',
            message='Ошибка, некорректное имя',
            code='Invalid'
        )
    ])
    secname = models.CharField( ("secname"), max_length=20, null=False, validators=[
        RegexValidator(
            regex=r'[A-ZА-Я]{1}[a-zа-я]{1,19}$',
            message='Ошибка, некорректная фамилия',
            code='Invalid'
        )
    ])
    phonenumber = models.CharField(("phonenumber"), max_length=11, null=False, validators=[
        RegexValidator(
            regex=r'[0-9]{11}',
            message='Ошибка, некорректный номер телефона',
            code='Invalid'
        )
    ])


