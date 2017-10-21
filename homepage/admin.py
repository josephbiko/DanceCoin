# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Account,Festival,Tickets,Drinks

admin.site.register(Account)
admin.site.register(Festival)
admin.site.register(Tickets)
admin.site.register(Drinks)


# Register your models here.
