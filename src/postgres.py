import pandas as pd
from sqlalchemy import create_engine

# Your data as a pandas DataFrame
data = {
    'record': [41970, 41973, 41971, 41972, 41975, 41974, 41977, 41976, 41978, 41979, 41980, 41981, 41982],
    'Q1': [7, 4, 3, 6, 5, 3, 2, 10, 3, 5, 5, 10, 10],
    'q2': [1, 6, 8, 3, 10, 1, 6, 8, 7, 9, 4, 10, 1],
    'q4': [10, 5, 10, 7, 3, 6, 7, 6, 5, 7, 10, 3, 6],
    'q4.1': [2, 7, 8, 7, 10, 9, 7, 9, 7, 4, 3, 10, 1],
    'q5': [2, 5, 10, 2, 3, 4, 7, 7, 7, 3, 3, 3, 3],
    'q6': [1, 6, 8, 3, 10, 1, 6, 8, 7, 9, 4, 10, 1],
    'q7': [10, 5, 10, 7, 3, 6, 7, 6, 5, 7, 10, 3, 6]
}

df = pd.DataFrame(data)

# PostgreSQL database connection details
hostname = 'localhost'
database = 'MasterDb'
username = 'postgres'
password = '1234'
port = '5432'

# Create a connection to PostgreSQL
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database}')

# Define the table name and schema (if needed)
table_name = 'survey_data'  # Replace with your desired table name
schema_name = 'public'  # You can change the schema if you have a custom one

# Write the DataFrame to PostgreSQL, replacing the existing table if it exists
df.to_sql(table_name, engine, if_exists='replace', index=False, schema=schema_name)

print(f"Table '{table_name}' created and data inserted successfully!")
