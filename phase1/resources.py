from import_export import resources
from phase1.models import CostSummary,RoadCostSummary,BOQ,R1_1

class CostSummaryResource(resources.ModelResource):
    class meta:
        model = CostSummary

class RoadCostSummaryResource(resources.ModelResource):
	class meta:
		model = RoadCostSummary

class BOQResource(resources.ModelResource):
	class meta:
		model = BOQ

class R1_1Resource(resources.ModelResource):
	class meta:
		model = R1_1
