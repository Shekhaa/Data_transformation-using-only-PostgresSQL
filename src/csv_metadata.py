# Extract and create columns on the basis of Meta data present in File.
import pandas as pd
csv=pd.read_csv('src/meta_data.csv')

lists=csv['Columns'].to_list()
print(lists)
