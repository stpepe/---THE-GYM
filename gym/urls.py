from django.urls import path
from .views import *

urlpatterns = [
    path('', mainpage),
    path('kbgucalc/', kbgucalc),
    path('ajax/num', ajax_num),
]