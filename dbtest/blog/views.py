from django.shortcuts import render,render_to_response
from blog import models


def hello(request):
    mot ='hello there!'
    return render_to_response('index.html',locals())

# Create your views here.
def show(request):
    user_list = models.userinfo.objects.all()
    aget =models.userinfo.objects.get(name='tom')
    userdata = models.userinfo.objects.all().values('name')
   # mo = models.userinfo.objects.all().values_list('id','memo')
    return render_to_response('index.html',locals())

 