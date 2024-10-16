import pandas as pd
def getdata():
# Read the Excel file
    read_excel = pd.read_excel('src/Disney_data.xlsx', engine='openpyxl')
    Fix_null = read_excel.fillna(0)

    print(Fix_null.head())

    # 'Q4A': 'nil', 'Q4Br5oe': 'NIL', 'Q28': 'NIL', 'Q37r97oe': 'NIL'
    Fix_null['Q4A'] = Fix_null['Q4A'].replace(0, 'NIL')
    Fix_null['Q4Br5oe'] = Fix_null['Q4Br5oe'].replace(0, 'NIL')
    Fix_null['Q28'] = Fix_null['Q28'].replace(0, 'NIL')
    Fix_null['Q37r97oe'] = Fix_null['Q37r97oe'].replace(0, 'NIL')
    Fix_null=Fix_null.drop(['date'],axis=1)
    # Print to verify if replacement worked
    # print(Fix_null.head())

    # Fix_null.to_excel('src/Check3.xlsx', index=False)
    return Fix_null

