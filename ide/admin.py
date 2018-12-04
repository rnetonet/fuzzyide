from django.contrib import admin
from django.shortcuts import redirect

from .models import (
    CONorm,
    DeFuzzy,
    Function,
    FunctionCategory,
    FuzzyModel,
    Rule,
    System,
    TNorm,
    Variable,
)

from . import views

# Register your models here.
class SystemAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['pk']
    actions = ['process']

    def process(self, request, queryset):
        system = queryset.first()
        return redirect("process_system", pk=system.pk)

    process.short_description = "Process Fuzzy System"

admin.site.register(System, SystemAdmin)

admin.site.register(Variable)
admin.site.register(Function)
admin.site.register(Rule)

admin.site.register(FunctionCategory)
admin.site.register(TNorm)
admin.site.register(CONorm)
admin.site.register(DeFuzzy)
admin.site.register(FuzzyModel)
