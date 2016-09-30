#coding=utf-8

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from models import User

class UserForm(forms.Form):
    username=forms.CharField(label="yonghuming",max_length=100)
    password=forms.CharField(label='mima',widget=forms.PasswordInput())



def regist(req):
    if req.method =='POST':
        uf=UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username = username, password =password)
            return HttpResponse('regist success!!!')

    else:
        uf=UserForm()

    return render_to_response('regist.html',{'uf':uf})   


def login(req):
    if req.method == "POST":
        uf =UserForm(req.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            user =User.objects.filter(username__exact=username,password__exact=password)
            if  user:
                response=HttpResponseRedirect('/online/index')
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/online/login')    
    else:
        uf =UserForm()
    return render_to_response('login.html',{'uf':uf})


def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html',{'username':username})

def logout(req):
    response = HttpResponse('logout!!!')
    response.delete_cookie('username')
    return response            
