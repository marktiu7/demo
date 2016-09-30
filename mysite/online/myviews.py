from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response




def my_view(request):
    if request.method == 'POST':
       username=request.POST['username']
       password=request.POST['password']
       user = authenticate(username=username,password=password)
       if user is not None:
           if user.is_active:
               login(request,user)
               return HttpResponseRedirect('h.html')
    return render_to_response('login.html')         