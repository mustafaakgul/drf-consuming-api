from django.contrib import admin

from . models import SavedEmbeds, CartItem, Test

admin.site.register(SavedEmbeds)
admin.site.register(CartItem)
admin.site.register(Test)
