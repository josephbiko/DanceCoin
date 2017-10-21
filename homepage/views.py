# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import View,TemplateView
from models import Account,Tickets,Festival,Drinks,Purchase
# Create your views here.


class home(TemplateView):
    template_name = "homepage/../templates/registration/login.html"

    def get(self, request, *args, **kwargs):
        user = None
        account = None

        if request.user.is_authenticated():
            account = Account.objects.get(user=request.user)
            tickets = Tickets.objects.filter(account=account)
        else:
            return HttpResponseRedirect(reverse_lazy("login"))
        context = {"login": request.user.is_authenticated(), "user":account,"tickets":tickets}

        return (render(request,"homepage/home.html",context=context))

    def post(self,request,*args,**kwargs):
        print( request.POST)

        user = None
        if request.user.is_authenticated():
            user = Account.objects.get(user=request.user)
            if user.type == "shop":
                shopPost(self,request)

        context = {"login": request.user.is_authenticated(), "user":user}

        return render(request,"homepage/home.html",context=context)


def shopPost(self,request):
    post = {}
    for p in request.POST:
        post[p.encode("ascii")] = request.POST[p].encode("ascii")

    acc = Account.objects.get(hash=post["qr"])
    drink = Drinks.objects.get(type=post["drink"])
    Purchase.objects.create(account=acc,drink=drink,amount=post["amount"])
    acc.tokens=acc.tokens-drink.price*float(post["amount"])
    acc.save()



