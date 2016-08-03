#coding:utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('BD Test Tools')

def home(request):
    return render(request,'home.html')

def log_input(request):
    appid=request.GET['appid']
    uid =request.GET['uid']
    actionid=request.GET['actionid']
    itemtype=request.GET['itemtype']
    utype=request.GET['utype']
    return HttpResponse('appid:%s&uid:%s&actionid:%s&itemtype:%s&utype:%s&' % appid, uid, actionid, itemtype, utype)