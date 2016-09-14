from django.contrib import admin
from .models import FigurePrint, FigureUseRecord


# Register your models here.

@admin.register(FigurePrint)
class FigurePrintAdmin(admin.ModelAdmin):
    pass


@admin.register(FigureUseRecord)
class FigureUseRecordAdmin(admin.ModelAdmin):
    pass
