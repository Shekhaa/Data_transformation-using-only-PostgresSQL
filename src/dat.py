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
table_name = 'dynamic2_table'
columns = ','.join([f"{col} {map_dtype(df[col].dtype)}" for col in df.columns])
create_table_query = f"CREATE TABLE {table_name} ({columns});"

print(columns)