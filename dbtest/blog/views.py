from django.shortcuts import render,render_to_response


def hello(request):
    mot ='hello there!'
    return render_to_response('index.html',locals())

# Create your views here.
