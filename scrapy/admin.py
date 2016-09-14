from django.contrib import admin
from .models import ScrapyContent, ScrapyTable


# Register your models here.
@admin.register(ScrapyContent)
class ScrapyContentAdmin(admin.ModelAdmin):
    pass


@admin.register(ScrapyTable)
class ScrapyTableAdmin(admin.ModelAdmin):
    pass
