# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View,TemplateView
from models import account
# Create your views here.


class home(TemplateView):
    template_name = "homepage/login.html"

    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated():
            user = account.objects.get(user=request.user)

        context = {"login": request.user.is_authenticated(), "user":user}
        return render(request,"homepage/home.html",context=context)

    def post(self,request,*args,**kwargs):
        print(request.POST)

        user = None
        if request.user.is_authenticated():
            user = account.objects.get(user=request.user)
            if user.type == "shop":
                shopPost(self,request)

        context = {"login": request.user.is_authenticated(), "user":user}

        return render(request,"homepage/home.html",context=context)


def shopPost(self,request):
    print(request.POST)

