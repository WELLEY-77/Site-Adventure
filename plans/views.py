from django.shortcuts import render
from django.http import HttpResponse


def plans(request):
    return render(request, 'plans/index.html')