from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Letters

@admin.register(Letters)
class LettersAdmin(admin.ModelAdmin):
    list_display = ('letters',)

