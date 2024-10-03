import psycopg2
import pandas as pd
# Database connection details
hostname = 'localhost'
database = 'MasterDb'
password = '1234'
username = 'postgres'
port_id = '5432'

curr = None
conn = None
string='y'
try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=password, port=port_id)
    
    # Create a cursor object
    curr = conn.cursor()
    
    # SQL script to create the table if it doesn't exist
    create_script = '''
    CREATE TABLE IF NOT EXISTS Data(
        id INT PRIMARY KEY NOT NULL,
        name VARCHAR(50),
        course VARCHAR(10)
    )
    '''
    
    curr.execute(create_script)
    
    while(string.lower()=='y'):
        id=int(input("Enter Id: ")) 
        course=input("Enter Course: ")
        name=input("Enter name: ")
        # Execute the SQL script
        insert_query='''INSERT INTO DATA(id,name,course) VALUES (%s,%s,%s)'''
        curr.execute(insert_query,(id,name,course))

        #values 
        string=input("want to enter more type y/n:")


    update_query='''UPDATE DATA SET course='Unknown',SET name='Unkown' WHERE course='' or name='' 
    '''
    
    curr.execute(update_query)
    # Commit the changes to the database
    
    conn.commit()
    
    print("Table created successfully!")

except Exception as error:
    print(error)

finally:
    # Close the cursor and connection
    if curr is not None:
        curr.close()
    if conn is not None:
        conn.close()


#use the pandas for data cleaning
