from django_audit_fields.admin import audit_fieldset_tuple

from .modeladmin import CrfModelAdmin


class ComplicationsAdmin(CrfModelAdmin):

    fieldsets = (
        (
            "Eye Examination",
            {
                "fields": (
                    'cataracts',
                    'fundoscopy',
                )
            },
        ),
        (
            "Foot Exam",
            {
                "fields": (
                    'achilles_tendon_reflex',
                    'foot_pin_prick',
                    'foot_light_touch',
                    'temperature_perception',
                )
            },
        ),
        (
            "Peripheral pulses",
            {
                "fields": (
                    'dorsalis_pedis_pulse',
                    'posterior_tibial_pulse',
                )
            },
        ),
        audit_fieldset_tuple,
    )
