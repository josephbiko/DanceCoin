# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    currency = models.FloatField(default=0)





