from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'startbootstrap-grayscale-gh-pages/index.html')

def privacy(request):
    return render(request, 'privacy-policy.html')
