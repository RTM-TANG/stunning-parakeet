""" Admin settings and permissions """

from django.contrib import admin

from .models import Item, Stock, Commission

admin.site.register(Item)
admin.site.register(Stock)
admin.site.register(Commission)