from django.contrib import admin
from .models import AttendTable, AttendPerson


# Register your models here.
@admin.register(AttendTable)
class AttendTableAdmin(admin.ModelAdmin):
    pass


@admin.register(AttendPerson)
class AttendPersonAdmin(admin.ModelAdmin):
    pass
