from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import User, Tema, Stat


@admin.register(User)
class GroupAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple}
    }
    search_fields = ("name", "city", "subs", "kids", "animals")
    ordering = ("name",)
    list_display = ['name', 'apruve', 'city', 'subs', 'link']

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ['count', 'date']


admin.site.register(Tema)
