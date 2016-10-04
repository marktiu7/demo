from django.shortcuts import render,render_to_response
from blog.models import *
from pub_form.pubform import *
from django.http import HttpResponse


def register(req):
    if req.method =='POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            print username,password
            return HttpResponse('ok')
    else:
        uf = UserForm()
    return  render_to_response('index.html',{'uf':uf})       
# Create your views here.
