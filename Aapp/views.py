from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Joke

def index(request):
    jokes = Joke.objects.all()

    # jokes = {'jokes': jokes}
    # пагинация
    paginator = Paginator(jokes, 2)
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)
    return render(request, 'index.html', {'jokes': jokes, 'items': items})




