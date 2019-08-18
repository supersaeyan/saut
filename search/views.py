from django.http import JsonResponse
from .models import clookup, lookup
from .validations import valid_word


def search(request):
    word = request.GET['word']
    word = word.lower()

    if not valid_word:
        return JsonResponse({'status': 'Invalid input'}, status=400)

    if 'naive' in request.GET:
        if request.GET['naive'].lower() == 'true':
            matches = lookup(word)
        else:
            # If naive arg passed as False
            matches = clookup(word)
    else:
        # If naive arg not passed
        matches = clookup(word)

    return JsonResponse(matches, safe=False, status=200)
