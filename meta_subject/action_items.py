from meta_ae.constants import AE_INITIAL_ACTION
from edc_action_item import Action, site_action_items
from edc_constants.constants import YES, HIGH_PRIORITY

from .constants import BLOOD_RESULTS_ACTION, RECONSENT_ACTION


class BloodResultAction(Action):
    name = BLOOD_RESULTS_ACTION
    display_name = "Reportable Blood Result"
    reference_model = "meta_subject.bloodresult"
    priority = HIGH_PRIORITY
    show_on_dashboard = True
    create_by_user = False

    def reopen_action_item_on_change(self):
        return False

    def get_next_actions(self):
        next_actions = []
        if (
            self.reference_obj.results_abnormal == YES
            and self.reference_obj.results_reportable == YES
        ):
            # AE for reportable result, though not on DAY1.0
            next_actions = [AE_INITIAL_ACTION]
        return next_actions


class ReconsentAction(Action):
    name = RECONSENT_ACTION
    display_name = "Re-consent participant"
    reference_model = "meta_subject.subjectreconsent"
    priority = HIGH_PRIORITY
    show_on_dashboard = True
    show_link_to_changelist = True
    admin_site_name = "meta_subject_admin"
    create_by_user = False
    singleton = True
    instructions = (
        "Participant must be re-consented as soon as able. "
        "Participant's ICF was initially completed by next-of-kin."
    )

    def reopen_action_item_on_change(self):
        return False


site_action_items.register(BloodResultAction)
site_action_items.register(ReconsentAction)
