# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import problems,admin_update,Postrequest,galley,stock_details,register

        
admin.site.register(register)
admin.site.register(problems)
admin.site.register(admin_update)
admin.site.register(Postrequest)
admin.site.register(galley)
admin.site.register(stock_details)
# Register your models here.
