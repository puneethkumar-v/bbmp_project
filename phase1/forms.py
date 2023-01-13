from django import forms
from bbmpapp.models import CostSummary, Post
from bbmpapp.resources import RoadResource
from django.utils.translation import gettext_lazy as _

import re

class CostSummaryForm(forms.Form):
    class meta:
        model = CostSummary
        fields = '__all__'


