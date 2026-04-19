from django.contrib import admin

from .models import Choice, Lifestyle, UserChoice

admin.site.register(Lifestyle)
admin.site.register(Choice)
admin.site.register(UserChoice)
