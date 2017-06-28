# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Approval,Source

# Register your models here.
admin.site.register(Approval)
admin.site.register(Source)
