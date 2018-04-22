from django.contrib import admin
from .models import APKFile


class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'package_name', 'package_version_code')


admin.site.register(APKFile, FileAdmin)
