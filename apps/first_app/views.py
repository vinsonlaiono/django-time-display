from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
# def index(request):

#     return render(request, "first_app/index.html")
def index(request):
    context = {
        # "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime())
    }
    return render(request,'first_app/index.html', context)

def yourMethodFromUrls(request):
    context = {
        "somekey":"somevalue"
    }
    return render(request,'first_app/page.html', context)
