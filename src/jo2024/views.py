from django.shortcuts import render
from datetime import datetime


def index(request):
    date = datetime.now()
    return render(request, "index.html", context={"date": date})