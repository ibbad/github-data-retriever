import json
import requests

from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello world')


def test(request):
    return HttpResponse('Test page')


def profile(request):
    parsed_data = []
    if request.method == "POST":
        username = request.POST.get("user")
        users = username.replace(' ', '').split(',')
        for u in users:
            req = requests.get('https://api.github.com/users/{}'.format(u))
            json_list = []
            json_list.append(json.loads(req.content.decode('utf-8')))
            user_data = {}
            for d in json_list:
                if d.get('name') is None:
                    continue
                else:
                    for key in d.keys():
                        user_data[key] = d.get(key)
                    parsed_data.append(user_data)
    return render(request, 'app/profile.html', {'data': parsed_data})
