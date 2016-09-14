from django.contrib import admin
from .models import Department, Job


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
