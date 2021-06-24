from django.contrib import admin

from .models import Step


class StepAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "number",
        "created_at",
        "updated_at"
    )
    ordering = ("-created_at",)
    fields = (
        "id",
        "number",
        "created_at",
        "updated_at"
    )


admin.site.register(Step, StepAdmin)
