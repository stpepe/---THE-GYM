from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Phonenumbers


def mainpage(request):
    return render ( request, 'gym/mainpage.html')

def kbgucalc(request):
    return render ( request, 'gym/kbgucalc.html')

@csrf_exempt
def ajax_num(request):
    phone_number = request.POST['phone']
    guy = Phonenumbers(phonenumber=request.POST['phone'],name=request.POST['name'],secname=request.POST['secname'])
    if not Phonenumbers.objects.filter(phonenumber=phone_number).exists():
        try:
            guy.full_clean()
        except ValidationError:
            print(ValidationError)
            return HttpResponse(500)
        else:
            guy.save()
            return HttpResponse(200)
    else:
        print("Этот номер телефона уже получает уведомления")
