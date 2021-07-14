from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def discography(request):
    return render(request, 'discography.html')

def videos(request):
    return render(request, 'videos.html')