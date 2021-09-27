from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Courses, Sections, Lectures

# admin.site.register([Courses, Sections, Lectures])
@admin.register(Courses, Sections, Lectures)
class ViewAdmin(ImportExportModelAdmin):
    pass