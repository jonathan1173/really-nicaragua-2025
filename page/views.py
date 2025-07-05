from django.shortcuts import render

# Create your views here.
def page_index(request):
    return render(request, 'rally_nicaragua/index/index.html')

def page_home(request):
    return render(request, 'page/home.html')