from django.contrib import admin
from .models import SystemUser, Worker


# Register your models here.
@admin.register(SystemUser)
class SystemUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    pass
