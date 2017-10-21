# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=64,default="client")
    tokens = models.FloatField(default=0)
    hash = models.CharField(max_length=64,default="81DBBQ837AERB0MYVTN5DG1BBL3B8XH5ILO7P84YPQQS81PFLGUN0QWHQHY1HJZ0")

class Festival(models.Model):
    name = models.CharField(max_length=64,default="ADE")
    price = models.FloatField(default=100)
    date = models.DateField(default=now)



class Tickets(models.Model):
    account = models.ForeignKey(Account,null=False)
    festival = models.ForeignKey(Festival,null=False)
    price = models.FloatField(default=100)





