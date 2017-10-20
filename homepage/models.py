# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    tokens = models.FloatField(default=0)
    hash = models.CharField(max_length=64,default="81DBBQ837AERB0MYVTN5DG1BBL3B8XH5ILO7P84YPQQS81PFLGUN0QWHQHY1HJZ0")




