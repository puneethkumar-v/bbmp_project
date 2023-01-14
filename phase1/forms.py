from django import forms
from phase1.models import CostSummary, RoadCostSummary,BOQ, R1_1,Post
from phase1.resources import RoadResource
from django.utils.translation import gettext_lazy as _

import re

class CostSummaryForm(forms.Form):
    class meta:
        model = CostSummary
        fields = '__all__'
class RoadCostSummaryForm(forms.Form):
    class meta:
        model = RoadCostSummary
        fields = '__all__'
class BOQForm(forms.Form):
    class meta:
        model = BOQ
        fields = '__all__'
class R1_1Form(forms.Form):
    class meta:
        model = R1_1
        fields = '__all__'



