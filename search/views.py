from django.http import JsonResponse
from .models import lookup


def search(request):
    word = request.GET['word']
    matches = lookup(word)
    return JsonResponse(matches, safe=False)
