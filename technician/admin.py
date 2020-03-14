# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import technician,notifications,admin_notify,reports

admin.site.register(technician)
admin.site.register(notifications)
admin.site.register(admin_notify)
admin.site.register(reports)
# Register your models here.
