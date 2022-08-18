import os
from django.conf import settings
from django.shortcuts import render


# Create your views here.
'''
def post_list(request):
    return render(request, os.path.join(settings.BASE_DIR, '/templates/index.html'), {})
'''
location = os.path.join(settings.BASE_DIR, 'templates\index.html')


def post_list(request):
    return render(request, location, {})
