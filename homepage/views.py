from django.shortcuts import render
from .models import HomePage


def index(request):
    content = HomePage.objects.get(id=1)
    return render(request, 'homepage/index.html', {'content': content})
