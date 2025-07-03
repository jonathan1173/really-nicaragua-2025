from django.shortcuts import render

# Create your views here.
def page_index(request):
    return render(request, 'base.html')

def page_home(request):
    return render(request, '/home/home.html')