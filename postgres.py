import pandas as pd
from sqlalchemy import create_engine
import newfile

# Example dataframe
data =newfile.fetch()
print(data)
df = pd.DataFrame(data)


# PostgreSQL database connection details
hostname = 'localhost'
database = 'MasterDb'
username = 'postgres'
password = '1234'
port = '5432'


engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database}')

df.to_sql('grouped_data', engine, if_exists='replace', index=True)

print("Data saved to PostgreSQL successfully!")
