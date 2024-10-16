import pandas as pd
from sqlalchemy import create_engine
import src/'data'

# Example dataframe
dataa =data.datafromApi()
print(dataa)
df = pd.DataFrame(dataa)



# PostgreSQL database connection details
hostname = 'localhost'
database = 'MasterDb'
username = 'postgres'
password = '1234'
port = '5432'



engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database}')

df.to_sql('Api_data', engine, if_exists='replace', index=True)

print("Data saved to PostgreSQL successfully!")
