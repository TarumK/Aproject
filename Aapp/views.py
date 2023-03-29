from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
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


def like(request, id):
    joke = get_object_or_404(Joke.objects.filter(pk=id))
    # print('Pf[jl d aeyrwb. ghtlcnfdktybz')
    # if request.is_ajax():
    # if request.is_ajax() or request.method == 'POST':
        # увеличиваем рейтинг шутки на 1
    joke.rating += 1
    joke.save()

        # возвращаем обновленный рейтинг в формате json
    data = {'rating': joke.rating}
    return JsonResponse(data)


def dislike(request, id):
    joke = get_object_or_404(Joke.objects.filter(pk=id))
    # print('Pf[jl d aeyrwb. ghtlcnfdktybz')
    # if request.is_ajax():
    # if request.is_ajax() or request.method == 'POST':
        # увеличиваем рейтинг шутки на 1
    joke.rating -= 1
    joke.save()

        # возвращаем обновленный рейтинг в формате json
    data = {'rating': joke.rating}
    return JsonResponse(data)
