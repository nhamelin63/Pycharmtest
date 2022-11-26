from django.shortcuts import render
from .models import news

# Create your views here.
def index(request):
    model = news.objects.all()
    return render(request, 'index.html', {'news': model})
