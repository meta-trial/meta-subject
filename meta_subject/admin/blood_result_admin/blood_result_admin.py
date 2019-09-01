from django.contrib import admin
from edc_action_item import action_fields
# from edc_model_admin import audit_fieldset_tuple

from ...admin_site import meta_subject_admin
from ...models import BloodResult
from ..modeladmin import CrfModelAdmin


@admin.register(BloodResult, site=meta_subject_admin)
class BloodResultsAdmin(CrfModelAdmin):

    # form = BloodResultForm

    readonly_fields = ("summary",) + action_fields

    list_display = ("abnormal", "reportable", "action_identifier")

    list_filter = ("results_abnormal", "results_reportable")

    search_fields = ("action_identifier",
                     "subject_identifier", "tracking_identifier")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "appointment" and request.GET.get("appointment"):
            kwargs["queryset"] = db_field.related_model.objects.filter(
                pk=request.GET.get("appointment", 0)
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
