# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View,TemplateView
from models import account
# Create your views here.
class home(TemplateView):
    template_name = "homepage/login.html"

    def get(self, request, *args, **kwargs):
        context = {"login": request.user.is_authenticated(), "user":account.objects.get(user=request.user)}

        return render(request,"homepage/home.html",context=context)