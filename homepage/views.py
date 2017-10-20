# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):

    context = {"login":request.user.is_authenticated(),}
    return render(request, 'homepage/home.html', context)