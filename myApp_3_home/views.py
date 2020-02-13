from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    #return HttpResponse("myapp2")

    return render(request, "index.html")

def index_action(request):
    #return HttpResponse("myapp2")

    response = HttpResponseRedirect('/algo1/')
    return response
