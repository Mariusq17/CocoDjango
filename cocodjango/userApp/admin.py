from django.contrib import admin

from .models import Employee, Language, LanguagesUsed

# Register your models here.
admin.site.register(Employee)
admin.site.register(Language)
admin.site.register(LanguagesUsed)
