from django.shortcuts import render

# Create your views here.


def test(request):
    return render(request,'mainapp/test.html')


def index(request):
    return render(request,'mainapp/index.html')


def about(request):
    return render(request,'mainapp/about.html')


def service(request):
    return render(request,'mainapp/service.html')
