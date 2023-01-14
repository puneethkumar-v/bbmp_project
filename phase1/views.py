from django.shortcuts import render
#import pandas as pd
from phase1.models import CostSummary,RoadCostSummary,BOQ, R1_1
from tablib import Dataset
from phase1.resources import CostSummaryResource,RoadCostSummaryResource,BOQResource


#def home(request):
    # f = pd.ExcelFile(
    #     '/home/puneethkumarv/Documents/python-project/bbmp_project/phase1/static/package.xlsx')
    # list_of_dfs = []
    # for sheet in f.sheet_names:

    #     # Parse data from each worksheet as a Pandas DataFrame
    #     df = f.parse(sheet)
    #     print(df)

    # # And append it to the list
    #     list_of_dfs.append(df)

    # # Combine all DataFrames into one
    # data = pd.concat(list_of_dfs, ignore_index=True)
    # # print(data)
    # # Preview first 10 rows
    # excel_data = data.head(10).to_json()
    # # print(data.head(10).to_dict().values())
    # # excel_data = data
    # df = pd.read_excel(
    #     '/home/puneethkumarv/Documents/python-project/bbmp_project/phase1/static/package.xlsx')
    # print(df.columns.ravel())
    # print(df)
    # out = df.to_numpy().tolist()
    # print(out)
    # out = [tuple(elt) for elt in out]
    # print(out)
def importExcel(request):
	if request.method == 'POST':
		#cost_summary_resource=CostSummaryResource()
		dataset1 = Dataset()
		new_cost_summary = request.FILES["my_file1"]
		imported_data1 = dataset1.load(new_cost_summary.read(),format='xlsx')
		for data in imported_data1:
			value = CostSummary(
				data[0],
				data[1],
				data[2],
				data[3]
				
			)
			value.save()
		#road_cost_summary_resource = RoadCostSummaryResource()
		dataset2 = Dataset()
		new_road_cost_summary = request.FILES["my_file2"]
		imported_data2 = dataset2.load(new_road_cost_summary.read(),format='xlsx')
		for data in imported_data2:
			value = RoadCostSummary(
				data[0],
				data[1],
				data[2],
				data[3],
				data[4]
				
				)
			value.save()
		#boq_resource=BOQResource()
		dataset3 = Dataset()
		new_boq = request.FILES["my_file3"]
		imported_data3 = dataset3.load(new_boq.read(),format='xlsx')
		for data in imported_data3:
			value = BOQ(
				data[0],
				data[1],
				data[2],
				data[3],
				data[4],
				data[5]
				)
			
			value.save()
		dataset4 = Dataset()
		new_r1_1 = request.FILES["my_file4"]
		imported_data4 = dataset4.load(new_r1_1.read(),format='xlsx')
		for data in imported_data4:
			value = R1_1(
				data[0],
				data[1],
				data[2],
				data[3],
				data[4]
				)
			
			value.save()
		

	return render(request,'form.html')
