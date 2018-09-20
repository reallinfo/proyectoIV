
# from django.shortcuts import render
from django.http import JsonResponse
from random import random

def test(request):
    return JsonResponse({'status':'ok'})


def random_number(request):
    return JsonResponse({'random_number':random()})
