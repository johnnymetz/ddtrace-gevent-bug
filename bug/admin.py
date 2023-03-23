from django.contrib import admin

from bug.models import FileObject


@admin.register(FileObject)
class FileObjectAdmin(admin.ModelAdmin):
    pass
