from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello World! i change it '
    return render(request, 'hello.html', context)
    #return HttpResponse("Hello world ! ")