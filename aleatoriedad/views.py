
# from django.shortcuts import render
from django.http import JsonResponse
from random import randint

def test(request):
    return JsonResponse({'status':'ok'})


def random_number(request):
    try:
        min = int(request.GET['min'])
        max = int(request.GET['max'])
        n = randint(min, max)
    except Exception as e:
        return JsonResponse({'error':'Invalid input'}, status = 400)

    return JsonResponse({'random_number':n}, status = 200)
