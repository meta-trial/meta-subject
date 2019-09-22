from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ...admin_site import meta_subject_admin
from ...forms import BloodResultsGluForm
from ...models import BloodResultsGlu
from .blood_results_modeladmin_mixin import (
    BloodResultsModelAdminMixin,
    conclusion_fieldset,
    summary_fieldset,
)


@admin.register(BloodResultsGlu, site=meta_subject_admin)
class BloodResultsGluAdmin(BloodResultsModelAdminMixin):

    form = BloodResultsGluForm

    autocomplete_fields = ["hba1c_requisition"]

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "HbA1c",
            {
                "fields": [
                    "is_poc",
                    "hba1c_requisition",
                    "hba1c_assay_datetime",
                    "hba1c",
                    "hba1c_units",
                    "hba1c_abnormal",
                    "hba1c_reportable",
                ]
            },
        ),
        conclusion_fieldset,
        summary_fieldset,
        audit_fieldset_tuple,
    )

    radio_fields = {"is_poc": admin.VERTICAL}