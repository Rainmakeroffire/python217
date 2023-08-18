from django.shortcuts import render

from .models import Work


def index(request):
    work = Work.objects.all()
    return render(request, 'index.html', {'works': work})
