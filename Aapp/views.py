from django.shortcuts import render
from .models import Joke

def index(request):
    jokes = Joke.objects.all()

    # jokes = {'jokes': jokes}
    return render(request, 'index.html', {'jokes': jokes})




