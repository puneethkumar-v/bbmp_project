from import_export import resources
from bbmpapp.models import CostSummary

class CostSummaryResource(resources.ModelResource):
    class meta:
        model = CostSummary
