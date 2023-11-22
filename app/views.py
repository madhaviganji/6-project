from django.shortcuts import render

# Create your views here.


def conditions(request):
    d={'a':10,'b':320,'c':450}
    return render(request,'conditions.html',d)
