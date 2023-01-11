from django.shortcuts import render
import pandas as pd


def home(request):
    f = pd.ExcelFile(
        '/home/puneethkumarv/Documents/python-project/bbmp_project/phase1/static/package.xlsx')
    list_of_dfs = []
    for sheet in f.sheet_names:

        # Parse data from each worksheet as a Pandas DataFrame
        df = f.parse(sheet)

    # And append it to the list
        list_of_dfs.append(df)

    # Combine all DataFrames into one
    data = pd.concat(list_of_dfs, ignore_index=True)

    # Preview first 10 rows
    excel_data = data.head(10).to_json()
    print(data.head(10).to_dict().values())

    return render(request, 'base.html', {"excel_data": excel_data})
