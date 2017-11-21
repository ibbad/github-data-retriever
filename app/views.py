import json
import requests

from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello world')


def test(request):
    return HttpResponse('Test page')


def profile(request):
    data = []
    req = requests.get('https://api.github.com/users/ibbad')
    data.append(json.loads(req.content.decode('utf-8')))
    parsed_data = []
    user_data = {}
    for d in data:
        for key in d.keys():
            user_data[key] = d.get(key)
    parsed_data.append(user_data)
    return render(request, 'app/profile.html', {'data': parsed_data})
