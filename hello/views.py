from django.shortcuts import render

from hello.models import Lunbo


def index(request):
    films = Lunbo.objects.all().values('id', 'name', 'image', 'title')
    return render(request, 'index.html', locals())
# Create your views here.
