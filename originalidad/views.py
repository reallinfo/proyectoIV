
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("""'test.html'""")
    return render(request, 'index.html', {})
