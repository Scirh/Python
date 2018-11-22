# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Hosts,Group,Module,Args
# Register your models here.

admin.site.register(Hosts)
admin.site.register(Module)
admin.site.register(Group)
admin.site.register(Args)


