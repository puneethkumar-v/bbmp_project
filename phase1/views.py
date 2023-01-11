from django.shortcuts import render
import pandas as pd


def home(request):
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
    df = pd.read_excel(
        '/home/puneethkumarv/Documents/python-project/bbmp_project/phase1/static/package.xlsx')
    print(df)
    out = df.to_numpy().tolist()
    print(out)
    out = [tuple(elt) for elt in out]
    print(out)

    return render(request, 'base.html', {"excel_data": out})
