"""
from edc_utils.model_builder import ModelBuilder
from meta_subject.forms_data.complications import txt

model_name = "Complications"
verbose_name = "Presence of Complications"
verbose_name_plural="Presence of Complications"

m = ModelBuilder(model_name, verbose_name=verbose_name, verbose_name_plural=verbose_name_plural)
m.add(txt)
m.p()

"""

txt = {}
txt.update(cataracts="""Presence of cataracts
1 = YES
2 = NO
""")
txt.update(fundoscopy="""Fundoscopy
1 = No retinopathy
2 = Background retinopathy
3 = Pre-proliferative retinopathy
4 = Proliferative retinopathy
5 = Maculopathy
""")
txt.update(achilles_tendon_reflex="""Achilles tendon reflex
1 = Present
2 = Absent
""")
txt.update(foot_pin_prick="""Pin prick testing on foot
1 = Normal
2 = Abnormal
help_text=Can the patient distinguish between sharp and non-sharp?
""")
txt.update(foot_light_touch="""Light touch
1 = Normal
2 = Abnormal
help_text=Can the patient feel light pressure on the dorsum of the foot?
 """)
txt.update(temperature_perception="""Temperature perception
1 = Normal
2 = Abnormal
help_text=Can the patient distinguish between temperature on the dorsum of the foot?
""")
txt.update(
    vibration_perception="""Vibration perception
1 = Normal
2 = Abnormal
help_text=Can the patient distinguish vibration/no vibration when tuning fork is applied to the apex of the big toe?
""")

txt.update(
    dorsalis_pedis_pulse="""Dorsalis pedis pulse
1 = Present
2 = Absent
""")
txt.update(
    posterior_tibial_pulse="""Posterior tibial pulse
1 = Present
2 = Absent
""")
