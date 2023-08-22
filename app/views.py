from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *

def Insert_Topic(request):
    tn=input('enter topic_name :')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('data inserted')


def Insert_Webpage(request):
    tn=input('enter topic_name :')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name :')
    u=input('enter url :')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('data inserted')

def Insert_AR(request):
    tn=input('enter topic_name :')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name :')
    u=input('enter url :')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d=input('enter date :')
    a=input('enter author :')
    e=input('enter email :')
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a,email=e)[0]
    AO.save()
    return HttpResponse('data inserted')


