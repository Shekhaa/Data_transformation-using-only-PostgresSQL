import pandas as pd
def fetch():
        
    new=pd.read_csv('new.csv')
    new.dropna()    
    return new

fetch()

# print(new)

# print(type(new))
# print(new.head())
# print(new['Genres'])

# new.to_csv('transformed.csv',header=True)
# print(len(new))