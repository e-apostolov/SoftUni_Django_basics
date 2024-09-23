from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    context = {
        "current_time": datetime.now(),
        "person": {
            "age": 20,
            "height": 190,
        },
        "ids": ["432423", "fdsfg42543", "43532425gds"],
        "some_text": "Hello my name is Evgeni and I am developer.",
        "users": [
            "petar",
            "ivan",
            "georgi",
            "maria",
            "iva"
        ]
    }
    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create django project",
                "author": "Diyan Kalaydzhiev",
                "content": "I really don't know how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 1",
                "author": "",
                "content": "I really don't know how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 2",
                "author": "Diyan Kalaydzhiev",
                "content": "",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context)
