import pandas as pd
import psycopg2

# Step 1: Read CSV file
csv_file = 'src/Check_data300.csv'
df = pd.read_csv(csv_file)

# Step 2: Map Pandas dtypes to PostgreSQL data types
def map_dtype(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return 'INTEGER'
    elif pd.api.types.is_float_dtype(dtype):
        return 'FLOAT'
    elif pd.api.types.is_bool_dtype(dtype):
        return 'BOOLEAN'
    else:
        return 'TEXT'

# Step 3: Create dynamic SQL for table creation
table_name = 'dynamic_table'
columns = ', '.join([f"{col} {map_dtype(df[col].dtype)}" for col in df.columns])
create_table_query = f"CREATE TABLE {table_name} ({columns});"

# Step 4: Connect to PostgreSQL and execute the query
connection = psycopg2.connect(
    host="localhost",
    database="MasterDb",
    user="postgres",
    password="1234",
    port='5432'
)

cursor = connection.cursor()

# Execute create table statement
cursor.execute(create_table_query)
connection.commit()

# Step 5: Close connection
cursor.close()
connection.close()

print(f"Table '{table_name}' created successfully!")

