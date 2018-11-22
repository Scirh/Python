# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 主机组
class Group(models.Model):
    group = models.CharField(max_length=20)

    def __str__(self):
        return self.group

#主机信息
class Hosts(models.Model):
    hostname =models.CharField(max_length=20)
    ip_addr = models.CharField(max_length=15)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return self.hostname

#模块信息
class Module(models.Model):
    mod_name = models.CharField(max_length=50)

    def __str__(self):
        return self.mod_name

#模块参数
class Args(models.Model):
    mod_args = models.CharField(max_length=50)
    mod = models.ForeignKey(Module,on_delete=models.CASCADE)

    def __str__(self):
        return self.mod_args





















